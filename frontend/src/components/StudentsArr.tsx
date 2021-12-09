import { useEffect, useState } from "react";
import SeatCell from "./SeatCell";
import SeatTable from "./SeatTable";
import {division} from "../method/ArrayMethod"
import "./style/StudentsArr.css"



interface studentsData {
    stu_list : Array<object>;
    init_value : number;
    best_value : number;
}


interface Satisfaction {
    init: number;
    best: number;
}

type StudentsArrProps = {
    studentsData : studentsData
    columnNumber :number
}

function StudentsArr({ studentsData, columnNumber }:StudentsArrProps) {
    const [processedData, setProcessedData] = useState<Array<Array<object>>>([]);
    const [satisfaction, setSatisfaction] = useState<Satisfaction>({
        init: 0,
        best: 0,
    })

    useEffect(() => {
        const { stu_list, init_value, best_value } = studentsData
        setSatisfaction({
            ...satisfaction,
            init: init_value,
            best: best_value
        })

        setProcessedData(division([...stu_list], columnNumber));
    }, []);

    return (
        <div>
            <div className="satisfaction">
                <p>
                    초기 만족도{" "}
                    <span>{satisfaction.init}</span>
                </p>
                <p>
                    최적 만족도{" "}
                    <span>{satisfaction.best}</span>
                </p>
            </div>
            <SeatTable>
                {processedData.map((col, index) => (
                    <div key={index} style={{ margin: "0 5px 0 5px" }}>
                        {col.map((duo, index) => (
                            <SeatCell key={index} duo={duo} />
                        ))}
                    </div>
                ))}
            </SeatTable>
        </div>
    );
}

export default StudentsArr;
