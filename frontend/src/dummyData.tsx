interface DummyData {
    stu_list: Array<object>;
    init_value: number;
    best_value: number;
}


const dummyData:DummyData = {
    stu_list: [
        {
            student1: { id: 1, name: "홍성빈", rating: 11 },
            student2: { id: 2, name: "정보경", rating: 12 },
        },
        {
            student1: { id: 3, name: "정재민", rating: 21 },
            student2: { id: 4, name: "심인용", rating: 22 },
        },
        {
            student1: { id: 5, name: "이경민", rating: 31 },
            student2: { id: 6, name: "이새결", rating: 32 },
        },
        {
            student1: { id: 7, name: "서재은", rating: 41 },
            student2: { id: 8, name: "원준연", rating: 42 },
        },
        {
            student1: { id: 9, name: "정명언", rating: 51 },
            student2: { id: 10, name: "서경수", rating: 52 },
        },
        {
            student1: { id: 11, name: "구동용", rating: 61 },
            student2: { id: 12, name: "김영찬", rating: 61 },
        },
        {
            student1: { id: 11, name: "채영창", rating: 33 },
        },
    ],
    init_value: 10.123456,
    best_value: 50.123456
};

export default dummyData;
