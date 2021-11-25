import { useEffect, useState } from "react";
import SeatCell from "../components/SeatCell";
import SeatTable from "../components/SeatTable";
import "../ArrayMethod";

function StudentsArr({ studentsData, columnNumber }) {
    const [processedData, setProcessedData] = useState([]);

    useEffect(() => {
        console.log(studentsData.length);
        setProcessedData(studentsData.division(columnNumber));
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
