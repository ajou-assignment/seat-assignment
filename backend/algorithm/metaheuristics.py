import numpy as np
import random

class Search:
    def __init__(self, values):
        self.values = values
        self.tabu_length = 10   # Tabu List 길이
        self.tabu_list = []
        self.max_iter = 1000    # 최대 반복 횟수
        self.swap_count = 20    # 최초 Swap 자식 해 수
        self.shake_count = 0   # 최초 Shake 자식해 수
        self.improve_check_count = 50  # 횟수동안 개선 없으면 종료
        self.total_count = self.swap_count + self.shake_count
    
    # 전체 합계 계산
    def _fitness(self, solution):
        sum = 0
        for i in range(0, len(values), 2):
            sum += self.values[solution[i], solution[i + 1]]
            sum += self.values[solution[i + 1], solution[i]]
        return sum
    
    def _two_swap(self, solution):
        new_solution = solution.copy()
        while True:
            i = np.random.choice(range(0, len(solution)-1))
            j = np.random.choice(range(0, len(solution)-1))
            if i-j == 0:    # 동일 값 나온거 제외
                continue
            elif ((i % 2) == 0) & (i + 1 == j): # 옆자리 짝꿍과 자리교체 제외
                continue
            else:
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                break
                
        return new_solution, (i, j)

    def _section_shake(self, solution):
        new_solution = solution.copy()
        while True:
            i = np.random.choice(range(0, len(solution)-1))
            j = np.random.choice(range(0, len(solution)-1))
            direction = np.random.choice(range(0, 2))
            if i-j == 0:    # 동일 값 나온거 제외
                continue
            elif (i - 1 == j) | (i + 1 == j): # Swap 과 중복 방지
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

    def _get_neighbors(self, solution):
        candidate_list = []
        tabu_list = []

        n = 0
        while n < self.swap_count:
            candidate, tabu = self._two_swap(solution)
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                tabu_list.append(tabu)
                n += 1

        n = 0
        while n < self.shake_count:
            candidate = self._section_shake(solution)
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                n += 1
                
        return candidate_list, tabu_list
    
    def _eval_aspiration(self, candidate_list, tabu_list):

        solution = ""
        fitness_list = []
        
        for candidate in candidate_list:
            value = self._fitness(candidate)
            fitness_list.append(value)
            
        current_solution = candidate_list[0]
        current_value = fitness_list[0]

        # Remove candidate
        list_del = []
        for i in range(0, len(tabu_list)):
            value = fitness_list[i]
            if tabu_list[i] in tabu_list:
                if value > self.aspiration_level:
                    pass
                else:
                    list_del.append(i)
        list_del.reverse()
        for i in list_del:
            del candidate_list[i]
            del tabu_list[i]
            del fitness_list[i]

        # 전부 Tabu로 삭제된 경우
        if len(candidate_list) == 0:    
            return current_solution, current_value, solution

        # Evalute each candidate
        current_solution = candidate_list[0]
        current_value = fitness_list[0]
        for candidate, tabu, value in zip(candidate_list[:len(tabu_list)], tabu_list, fitness_list[0:len(tabu_list)]):
            if value > current_value:
                current_value = value
                current_solution = candidate
                current_tabu = tabu
                solution = "swap"
        
        for candidate, value in zip(candidate_list[len(tabu_list):], fitness_list[len(tabu_list):]):
            if value > current_value:
                current_value = value
                current_solution = candidate
                solution = "shake"

        if solution == "swap":
            # Update tabu list
            if len(self.tabu_list) < self.tabu_length:
                self.tabu_list.append(current_tabu)
            else:
                self.tabu_list.pop(0)
                self.tabu_list.append(current_tabu)
        
        return current_solution, current_value, solution

    def solve(self):
        # Initial solution
        initial_solution = list(np.random.permutation(range(0, len(self.values))))
        initial_value = self._fitness(initial_solution)
        
        # print(f"초기해 : {initial_value} / {initial_solution}")

        current_solution = initial_solution
        current_value = initial_value
        self.aspiration_level = initial_value
        
        # Initialize best value
        best_value = -np.inf
        best_solution = None

        # Same Value Count
        count_same_value = 0

        count_loop = 0
        while count_loop < self.max_iter:
            # Generate candidates
            candidate_list, tabu_list = self._get_neighbors(current_solution)
            
            # Evaluating tabu and aspiration
            current_solution, current_value, solution = self._eval_aspiration(candidate_list, tabu_list)

            if current_value <= best_value:
                count_same_value += 1
            else:
                count_same_value = 0
            
            if current_value > best_value:
                best_value = current_value
                best_solution = current_solution
                if best_value > self.aspiration_level:
                    self.aspiration_level = best_value
                if (solution == "swap") & (self.swap_count < self.total_count):
                    self.swap_count += 1
                    self.shake_count -= 1
                    # print(f"{count_loop} : {self.swap_count} / {self.shake_count}")
                if (solution == "shake") & (self.swap_count > 5):
                    self.swap_count -= 1
                    self.shake_count += 1
                    # print(f"{count_loop} : {self.swap_count} / {self.shake_count}")
            
            count_loop += 1

            if count_same_value == self.improve_check_count:
                break
        
        # print(f"{count_loop} :  {best_value} / {best_solution}")
        # for i in range(0,len(best_solution), 2):
        #     print('[' + studends[best_solution[i]] + ', ' + studends[best_solution[i + 1]] + ']', end=' ')

        # print(self.getSeatData(best_solution))
        print(f"init : {initial_value}")
        print(f"{count_loop} :  {best_value}")

        return best_solution

    # def getStudentData(self):

    #     return 1


def getSeatData():
    search = Search(values)
    best_solution = search.solve()
    listSeatDataAll = []
    for i in range(0,len(best_solution), 2):
        listSeatData = {
        "student1":{
            "id":best_solution[i] + 1, 
            "name":studends[best_solution[i]], 
            "rating":values[best_solution[i]][best_solution[i + 1]]},
        "student2":{
            "id":best_solution[i + 1] + 1, 
            "name":studends[best_solution[i + 1]], 
            "rating":values[best_solution[i + 1]][best_solution[i]]}
        }
        listSeatDataAll.append(listSeatData)
    return listSeatDataAll


# values = np.random.randint(0, 100, size=(24, 24))
# for i in range(0,24):
#     values[i,i] = 0
# print('[', end='')
# for i in range(0,24):
#     print('[', end='')
#     for j in range(0,24):
#         print(values[i,j], end=',')
#     print('],')
# print(']', end='')

# values = np.array([[0,48,71,89,25,7,43,44,4,83,14,75,87,4,32,45,25,70,26,17,46,85,96,34,0,0,8,68,64,57,94,23,83,35,93,22,11,24,97,71,],
# [86,0,17,50,10,40,33,6,20,30,30,57,42,14,1,82,82,16,75,77,51,12,88,9,87,13,79,77,20,76,53,64,51,71,81,52,99,61,79,95,],
# [46,99,0,2,68,11,86,1,19,22,37,89,15,9,29,72,0,63,85,52,46,69,84,56,27,11,41,60,43,79,20,74,2,4,51,65,51,55,83,97,],
# [70,50,59,0,65,81,30,98,77,21,96,13,93,50,13,47,97,63,61,21,30,44,94,56,37,83,26,28,46,70,63,90,24,60,72,97,49,73,84,37,],
# [37,20,9,83,0,83,21,38,18,59,57,37,95,97,37,75,12,6,2,34,93,18,17,8,27,67,33,96,36,16,1,53,29,69,68,50,62,26,10,23,],
# [36,2,23,9,13,0,35,56,81,8,88,87,94,33,63,61,49,24,65,54,93,89,34,39,75,20,49,3,0,54,79,96,3,78,11,47,91,78,87,9,],
# [40,5,60,87,81,40,0,1,39,87,83,42,81,92,14,40,97,60,4,18,36,79,83,22,16,16,51,56,14,59,28,78,54,9,36,22,96,45,78,82,],
# [21,88,44,46,8,18,23,0,74,48,59,38,90,15,10,75,98,17,62,62,66,70,91,94,98,39,68,49,31,0,65,91,18,44,41,58,57,11,98,15,],
# [36,46,85,31,67,55,56,37,0,23,40,95,90,56,30,30,23,12,97,4,10,47,45,15,30,24,85,78,42,57,15,15,83,88,10,19,47,29,33,62,],
# [36,66,44,40,57,43,38,13,21,0,30,25,81,79,35,95,81,56,25,47,19,1,61,95,61,21,82,25,95,43,63,86,19,1,39,7,22,41,2,85,],
# [12,80,41,27,58,34,52,39,62,33,0,50,56,27,35,68,70,28,34,34,76,60,73,80,94,23,83,0,79,20,57,83,13,18,64,65,41,60,6,28,],
# [78,59,59,4,37,45,63,47,70,24,72,0,65,32,71,50,88,8,98,64,81,17,26,26,3,87,56,89,33,58,49,56,91,86,24,35,42,43,5,41,],
# [59,97,59,48,65,38,62,71,54,77,89,61,0,36,67,46,56,88,49,94,43,19,68,72,99,38,92,94,37,28,18,41,24,66,84,3,4,64,19,64,],
# [68,22,14,72,96,34,53,1,58,97,27,27,79,0,88,89,15,62,25,74,43,64,51,46,27,65,45,68,48,70,5,28,88,12,81,45,94,53,77,22,],
# [33,96,94,84,80,18,17,53,40,28,5,48,21,38,0,45,24,76,42,2,49,92,2,13,50,55,4,65,2,81,43,33,39,24,75,41,12,51,3,84,],
# [42,42,82,77,61,33,91,92,39,75,27,39,15,65,66,0,80,30,4,30,0,73,70,71,39,75,42,50,85,2,53,61,64,36,64,13,16,52,73,23,],
# [56,71,34,79,54,39,97,74,34,64,45,19,33,22,60,41,0,28,21,47,29,95,11,76,50,40,61,2,33,96,64,54,89,58,58,73,68,71,41,90,],
# [36,45,96,29,11,19,56,40,34,56,43,18,84,73,91,81,43,0,58,10,57,14,99,91,5,95,60,47,73,18,96,45,18,26,65,1,95,75,29,65,],
# [97,73,70,3,13,29,15,48,97,19,59,15,86,0,53,50,37,82,0,38,80,12,41,87,90,85,30,56,81,58,79,72,52,27,59,78,29,84,42,81,],
# [12,55,16,4,17,99,91,82,59,19,90,46,84,99,97,10,10,41,84,0,14,38,5,12,96,8,17,33,81,3,10,24,8,6,62,99,11,47,67,57,],
# [77,14,45,66,63,66,39,4,18,31,34,15,27,8,22,4,13,66,14,47,0,73,53,28,15,15,43,27,86,48,71,41,53,53,51,61,72,67,57,32,],
# [21,24,80,39,60,33,33,69,66,88,1,28,9,37,81,9,88,95,59,42,80,0,70,25,68,83,46,24,33,13,49,33,15,38,18,59,56,21,34,65,],
# [77,57,81,46,2,59,84,98,65,28,7,80,3,66,85,62,70,42,79,83,72,33,0,0,10,43,6,65,85,73,58,97,24,16,13,16,91,27,59,58,],
# [18,28,62,33,93,44,71,58,65,85,78,39,3,36,29,51,84,90,79,32,81,84,80,0,3,18,34,34,56,87,46,23,83,93,24,25,75,23,73,28,],
# [52,63,77,71,89,21,75,51,32,86,79,14,4,73,67,16,6,38,92,87,90,74,99,66,0,58,28,46,63,47,84,42,97,67,84,48,19,6,81,45,],
# [25,70,95,30,91,15,39,27,87,8,75,2,15,81,41,20,68,1,37,29,47,13,78,32,67,0,47,74,20,56,43,95,79,48,85,21,0,98,1,14,],
# [22,82,64,95,42,92,97,12,8,28,42,73,15,35,0,86,98,37,38,44,68,18,13,17,43,79,0,43,48,0,3,58,69,1,92,35,67,78,11,74,],
# [46,45,27,88,41,94,75,77,34,66,39,25,77,81,59,94,44,89,60,40,41,72,56,5,17,20,89,0,0,1,24,85,63,25,5,75,32,10,98,95,],
# [80,36,55,46,18,2,80,73,91,73,96,34,25,74,63,9,86,19,10,56,0,68,6,17,54,77,37,35,0,50,35,54,50,2,57,17,78,24,79,75,],
# [89,1,78,24,82,44,36,20,10,45,44,33,50,39,43,4,73,84,76,89,34,18,91,73,32,60,27,91,58,0,0,41,43,61,91,34,51,84,67,29,],
# [71,12,17,71,69,71,52,74,61,39,95,70,30,28,36,61,55,40,26,54,43,52,95,2,76,74,55,31,24,21,0,37,96,99,22,27,43,25,25,6,],
# [32,60,47,69,11,86,14,26,27,34,42,77,28,40,28,21,76,81,87,87,47,60,56,59,27,63,63,45,81,45,4,0,50,42,80,13,50,27,69,77,],
# [83,94,5,79,99,54,84,52,95,24,73,61,93,92,78,70,6,3,80,54,80,96,68,73,30,56,60,40,71,82,83,12,0,61,9,94,61,90,18,87,],
# [79,73,67,87,84,22,76,69,14,58,40,91,83,19,63,46,49,56,41,39,17,77,86,90,59,65,51,10,48,33,66,75,56,0,24,33,55,29,45,11,],
# [55,16,91,92,54,45,92,3,61,92,72,56,99,80,4,39,34,49,19,46,48,9,37,30,39,56,13,84,58,66,26,15,65,68,0,96,67,93,57,37,],
# [44,23,53,71,43,50,78,12,19,89,70,90,29,88,78,88,9,64,84,23,78,33,57,82,26,27,49,25,53,27,22,44,33,82,24,0,75,14,14,47,],
# [93,79,20,0,42,2,71,77,43,72,6,60,90,89,0,42,5,91,43,20,28,78,70,84,63,26,72,60,80,79,20,1,90,5,40,74,0,34,91,47,],
# [69,6,88,1,11,68,28,3,50,13,15,15,64,85,24,56,76,31,27,38,55,70,7,7,19,34,69,35,44,83,13,19,99,40,24,45,25,0,23,26,],
# [5,86,71,9,62,6,21,32,34,6,40,48,93,29,98,3,13,96,57,70,89,24,45,77,66,22,75,63,52,91,42,73,91,49,15,88,0,51,0,29,],
# [61,13,91,80,6,34,12,3,53,65,86,79,6,83,32,34,94,34,25,9,77,8,29,22,85,37,78,61,63,21,30,6,6,7,56,7,25,64,51,-np.inf,]])

studends = np.array(['심인용', '이경민', '홍성빈', '정재민', '정보경', '서재은', '구동용', '강지혜', '노유정', '박봄', '박수정', '박윤우', '박주현', '배기운',
                     '서경수', '서동찬', '성원기', '원준연', '이창훈', '정명언', '박찬우', '장동찬', '김민주', '김영찬'])

values = np.array([
[-np.inf,48,74,7,93,40,78,81,27,49,75,73,38,35,80,21,24,31,11,65,89,44,60,83,],
[52,-np.inf,70,76,48,80,25,92,13,21,31,43,81,28,32,17,39,82,18,84,64,17,95,53,],
[46,45,-np.inf,67,66,57,40,63,40,1,53,36,38,58,78,11,76,89,33,30,3,38,52,29,],
[39,39,57,-np.inf,85,40,87,84,70,16,16,14,21,97,59,96,99,29,47,36,83,31,27,68,],
[46,23,37,73,-np.inf,48,5,65,34,55,5,38,69,12,48,76,56,90,80,80,20,12,21,62,],
[7,89,52,79,24,-np.inf,73,95,64,45,24,51,53,1,69,56,14,51,79,37,88,81,90,37,],
[20,71,53,72,70,24,-np.inf,2,26,76,28,75,40,37,54,98,51,25,17,92,90,10,29,22,],
[4,24,96,93,32,3,39,-np.inf,68,46,35,94,48,85,23,49,15,35,21,55,18,5,11,65,],
[1,1,80,11,44,13,86,90,-np.inf,59,5,99,83,53,99,3,72,77,27,52,19,29,84,4,],
[72,85,51,12,88,15,51,25,9,-np.inf,4,55,63,86,88,73,26,11,53,90,44,47,48,75,],
[53,36,75,63,41,21,75,78,77,79,-np.inf,15,13,87,52,0,93,99,59,76,54,44,0,59,],
[31,25,70,70,67,33,4,61,91,24,54,-np.inf,8,0,29,85,6,76,47,41,52,85,65,17,],
[92,88,86,10,82,36,83,95,38,94,29,55,-np.inf,92,99,87,67,57,20,13,68,44,74,41,],
[4,99,5,83,18,51,58,86,72,77,15,34,32,-np.inf,76,61,92,38,97,93,88,58,58,40,],
[64,37,3,51,50,52,81,80,36,47,54,97,78,85,-np.inf,7,18,25,75,11,74,40,13,84,],
[92,80,11,87,35,36,95,33,47,53,47,73,74,54,20,-np.inf,35,87,9,77,46,8,15,20,],
[22,14,22,25,62,65,1,29,58,79,11,80,83,9,97,65,-np.inf,58,81,0,78,42,57,77,],
[36,0,17,70,68,99,54,84,11,71,78,41,39,38,94,14,88,-np.inf,38,75,19,93,95,43,],
[18,57,76,2,16,39,55,8,48,82,79,45,33,31,20,31,5,66,-np.inf,88,23,30,67,80,],
[50,71,35,77,85,93,12,98,22,77,10,24,91,18,38,27,48,94,68,-np.inf,30,14,89,65,],
[93,56,41,11,33,33,12,12,12,79,33,46,82,61,58,44,88,57,96,59,-np.inf,27,57,65,],
[50,57,18,35,72,84,53,79,16,99,98,70,89,27,50,96,21,27,16,24,59,-np.inf,1,4,],
[90,30,1,89,44,62,77,41,64,76,28,19,16,69,39,52,31,91,58,37,32,68,-np.inf,78,],
[68,43,89,63,91,49,63,3,24,25,85,85,56,18,63,81,19,48,71,53,94,59,10,-np.inf,],
])

# values = np.array([[-np.inf, 73, 20, 27, 94,  7,  7, 51, 92, 21],
#         [28, -np.inf, 57, 31, 80, 69, 11, 10, 28, 39],
#         [45, 58, -np.inf, 31, 70, 74, 47, 40, 77, 11],
#         [13, 60,  2, -np.inf, 13, 74, 64, 96, 53, 10],
#         [50, 38, 49, 87, -np.inf, 78, 30, 36, 86, 56],
#         [94, 34, 15, 87, 97, -np.inf, 98, 89, 20, 17],
#         [64, 45, 89, 63, 85, 42, -np.inf,  7, 12, 79],
#         [74, 21, 87, 76, 26, 87, 34, -np.inf, 15, 44],
#         [48, 41, 81,  7, 50, 24,  7,  7, -np.inf, 96],
#         [15, 73, 60, 82, 79, 18, 54,  3, 54, -np.inf]])

import time
start = time.time()  # 시작 시간 저장
# for i in range(0,10):
#     search = Search(values, 10, 1000)
#     search.solve()
print(getSeatData())
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간