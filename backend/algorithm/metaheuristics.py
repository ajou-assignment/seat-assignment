from sys import api_version
import numpy as np
import random
from numpy.core.records import array
from api.dbSelect import *

table_Student = []
table_Rating = []
table_Recent = []

class Search:
    def __init__(self, listStudentData, option):
        self.listStudentData = listStudentData
        self.max_iter = 1000    # 최대 반복 횟수
        self.swap_count = 5    # 최초 Swap 자식 해 수
        self.shake_count = 5   # 최초 Shake 자식해 수
        self.improve_check_count = 100  # 횟수동안 개선 없으면 종료
        self.total_count = self.swap_count + self.shake_count
        self.EvalMethod = "Sum" # 목적함수 유형
        self.option = option    # Option

        if self.option == "Std":
            self.EvalMethod = "Std"

    # 적합도 계산 (목적 함수)
    def _fitness(self, solution):
        val = 0
        if self.EvalMethod == "Sum":
            val = self._fitness_Sum(solution)
        if self.EvalMethod == "Std":
            val = self._fitness_Std(solution)
        return val
    
    def _fitness_Sum(self, solution):   # 목적함수 : 합계 최대화
        sum = 0
        for i in range(0, len(solution), 2):
            sum += self.listStudentData[str(solution[i])]["rating"][str(solution[i + 1])]
            sum += self.listStudentData[str(solution[i + 1])]["rating"][str(solution[i])]
        return sum

    def _fitness_Std(self, solution):   # 목적함수 : 표준편차 최소화
        arr = np.array([])
        for i in range(0, len(solution), 2):
            arr = np.append(arr, self.listStudentData[str(solution[i])]["rating"][str(solution[i + 1])])
            arr = np.append(arr, self.listStudentData[str(solution[i + 1])]["rating"][str(solution[i])])
        return np.std(arr)
    
    def _multi_swap(self, solution):    # 멤버 30%를 섞음
        new_solution = solution.copy()
        swap_count = int(len(new_solution) * 0.3) # 이 갯수 이하의 요소가 섞임
        listSwapIndex = []
        listSwapValue = []

        while len(listSwapIndex) < swap_count:
            point = np.random.choice(range(0, len(new_solution)-1))
            if point not in listSwapIndex:
                listSwapIndex.append(point)
                listSwapValue.append(new_solution[point])

        listSwapIndex.sort()

        for idx, value in zip(listSwapIndex, listSwapValue) :
            new_solution[idx] = value

        return new_solution

    def _section_shake(self, solution): # 임의의 2명 사이를 섞음
        new_solution = solution.copy()
        while True:
            i = np.random.choice(range(0, len(solution)-1))
            j = np.random.choice(range(0, len(solution)-1))
            direction = np.random.choice(range(0, 2))
            if i-j == 0:    # 동일 값 나온거 제외
                continue
            elif (i - 1 == j) | (i + 1 == j): # 옆자리 둘이 바뀌는거 방지
                continue
            elif (i < j) & (direction == 0):
                section = new_solution[i:j]
                random.shuffle(section)
                new_solution = new_solution[:i] + section + new_solution[j:]
                break
            elif (i > j) & (direction == 0):
                section = new_solution[j:i]
                random.shuffle(section)
                new_solution = new_solution[:j] + section + new_solution[i:]
                break
            elif (i < j) & (direction == 1):
                section = new_solution[:i] + new_solution[j:]
                random.shuffle(section)
                new_solution = section[:i] + new_solution[i:j] + section[i:]
                break
            elif (i > j) & (direction == 1):
                section = new_solution[:j] + new_solution[i:]
                random.shuffle(section)
                new_solution = section[:i] + new_solution[j:i] + section[i:]
                break
                
        return new_solution

    def _get_neighbors(self, solution): #후보해 생성
        candidate_list = []

        n = 0
        while n < self.swap_count:
            candidate = self._multi_swap(solution)
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                n += 1

        n = 0
        while n < self.shake_count:
            candidate = self._section_shake(solution)
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                n += 1

        return candidate_list      
    
    def _eval_Candidate(self, candidate_list):  # 후보해 평가
        solution = ""
        fitness_list = []
        cnt_SolutionType = self.swap_count
        
        candidate_list, cnt_SolutionType = self.CheckConstraing(candidate_list, cnt_SolutionType)   # 제약조건 확인

        for candidate in candidate_list:    # 후보해 적합도 계산
            value = self._fitness(candidate)
            fitness_list.append(value)
            
        if len(candidate_list) == 0:    # 후보해 전부 제약조건으로 소거 시
            if self.EvalMethod == "Sum":
                return [], -np.inf, solution
            else:
                return [], np.inf, solution
        
        current_solution = candidate_list[0]
        current_value = fitness_list[0]
        for candidate, value in zip(candidate_list[:cnt_SolutionType], fitness_list[0:cnt_SolutionType]):
            if self.CheckImprove(value, current_value):
                current_value = value
                current_solution = candidate
                solution = "swap"
        
        for candidate, value in zip(candidate_list[cnt_SolutionType:], fitness_list[cnt_SolutionType:]):
            if self.CheckImprove(value, current_value):
                current_value = value
                current_solution = candidate
                solution = "shake"
        
        return current_solution, current_value, solution

    def CheckConstraing(self, candidate_list, cnt_SolutionType):    # 제약조건
        if(self.option == "recent"):
            for candidate in range(len(candidate_list) - 1, -1, -1) :
                for i in range(0, len(candidate_list[candidate]), 2):
                    if (candidate_list[candidate][i + 1] in self.listStudentData[str(candidate_list[candidate][i])]["recent"]) | (candidate_list[candidate][i] in self.listStudentData[str(candidate_list[candidate][i + 1])]["recent"]):
                        if candidate < cnt_SolutionType:
                            cnt_SolutionType = cnt_SolutionType - 1
                        candidate_list.remove(candidate_list[candidate])
                        break
        return candidate_list, cnt_SolutionType


    def solve(self):
        # Initial solution
        print(self.option)
        initial_solution = self.SetInitSolution()   # 초기해 생성 (랜덤)

        initial_value = self._fitness(initial_solution)

        # print(initial_value)
        
        current_solution = initial_solution
        current_value = initial_value
        
        # Initialize best value
        best_solution = current_solution
        best_value = current_value

        # Same Value Count
        count_same_value = 0

        count_loop = 0
        while count_loop < self.max_iter:
            # Generate candidates
            candidate_list = self._get_neighbors(best_solution)
            
            current_solution, current_value, solution = self._eval_Candidate(candidate_list)

            if self.CheckImprove(current_value, best_value):    # 개선 여부 확인
                count_same_value = 0
                best_value = current_value
                best_solution = current_solution
                if (solution == "swap") & (self.swap_count < self.total_count): # 최적해 개선에 기여한 Solution 가중치 증가
                    self.swap_count += 1
                    self.shake_count -= 1
                if (solution == "shake") & (self.swap_count > 5):   # 최적해 개선에 기여한 Solution 가중치 증가
                    self.swap_count -= 1
                    self.shake_count += 1
            else:
                count_same_value += 1   # 개선되지 않은 횟수 체크
            
            count_loop += 1

            if count_same_value == self.improve_check_count:
                break

        #print(best_value)

        return best_solution, initial_value, best_value

    def CheckImprove(self, current_value, best_value) : # 최적해 개선 여부 체크
        if ((self.EvalMethod == "Sum") & (current_value > best_value)) | ((self.EvalMethod == "Std") & (current_value < best_value)):
            return True
        else :
            return False

    def SetInitSolution(self):  # 초기해 생성 (랜덤)
        initial_solution = []
        for key, value in self.listStudentData.items():
            initial_solution.append(value['num'])
        random.shuffle(initial_solution)
        return initial_solution

def getSeatData(option):    # API 호출용 함수  
    # Database 데이터를 활용하여 Data 생성
    # print(option)
    table_Student = dbSelect('Select * from [api_student_info]')
    table_Rating = dbSelect('Select * from [api_satisfaction_point]')
    table_Recent = dbSelect('Select TOP(100) * from [api_hist_match] Order by [id] desc ')

    # print(len(table_Recent))

    listStudentData = getStudentData(table_Student, table_Rating, table_Recent)
    search = Search(listStudentData, option)
    best_solution, init_value, best_value = search.solve()
    listSeatDataAll = {}
    listSeatDataList = []
    for i in range(0,len(best_solution), 2):    # I/F를 위한 Data Set 생성
        listSeatData = {
            "student1":{
            "id":best_solution[i], 
            "name":listStudentData[str(best_solution[i])]["name"], 
            "rating":listStudentData[str(best_solution[i])]["rating"][str(best_solution[i + 1])]},
        "student2":{
            "id":best_solution[i + 1],
            "name":listStudentData[str(best_solution[i + 1])]["name"], 
            "rating":listStudentData[str(best_solution[i + 1])]["rating"][str(best_solution[i])]
            }
        }
        listSeatDataList.append(listSeatData)
        listSeatDataAll["stu_list"] = listSeatDataList
        dbSelect('Insert Into [api_hist_match] Values(' + str(best_solution[i]) + ', ' + str(best_solution[i + 1]) + ')')
    #listSeatDataAll.append(init_value)
    listSeatDataAll["init_value"] = init_value
    #listSeatDataAll.append(best_value)
    listSeatDataAll["best_value"] = best_value
    return listSeatDataAll

def getStudentData(table_Student, table_Rating, table_Recent):  # Database 데이터를 활용하여 Data 생성
    listStudentData = {}
    for student in table_Student:
        data = {
           "num" : student["stu_num"],
           "name" : student["stu_name"],
           "rating" : {},
           "recent" : []
        }
        listStudentData[str(student["stu_num"])] = data

    for rating in table_Rating :
        listStudentData[str(rating["stu_num_from"])]["rating"][str(rating["stu_num_to"])] = rating["point"]

    for recent in table_Recent :
        listStudentData[str(recent["stu_num1"])]["recent"].append(recent["stu_num2"])
        listStudentData[str(recent["stu_num2"])]["recent"].append(recent["stu_num1"])

    return listStudentData

