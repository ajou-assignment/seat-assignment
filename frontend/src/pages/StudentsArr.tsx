import { useEffect, useState } from "react";
import SeatCell from "../components/SeatCell";
import SeatTable from "../components/SeatTable";
import {division} from "../ArrayMethod"

type StudentsArrProps = {
    studentsData:Array<object>;
    columnNumber:number
}

function StudentsArr({ studentsData, columnNumber }:StudentsArrProps) {
    const [processedData, setProcessedData] = useState<Array<Array<object>>>([]);

    useEffect(() => {
        console.log(studentsData.length);
        setProcessedData(division([...studentsData], columnNumber));
    }, []);

    return (
        <div>
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
