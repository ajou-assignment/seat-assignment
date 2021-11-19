import { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import SeatCell from "../components/SeatCell";
import SeatTable from "../components/SeatTable";
import "../ArrayMethod";

function StudentsArr({ studentsData, columnNumber }) {
    const [processedData, setProcessedData] = useState([]);

    useEffect(() => {
        setProcessedData(studentsData.division(columnNumber));
    }, []);

    useEffect(() => {
        console.log(processedData);
    }, [processedData]);

    const clickButton = () => {
        console.log("심인용 바보");
        fetch("/students-data").then((res) => {
            console.log(res);
        });
    };

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
            <div>
                <Button onClick={clickButton}>Click me</Button>
            </div>
        </div>
    );
}

export default StudentsArr;
