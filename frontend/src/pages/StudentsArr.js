import { useEffect, useState } from "react";
import { Container, Button } from "react-bootstrap";
import Footer from "../components/Footer";
import Header from "../components/Header";
import SeatCell from "../components/SeatCell";
import SeatTable from "../components/SeatTable";
import tempData from "../tempData";
import "../ArrayMethod";

function StudentsArr({ columnNumber }) {
    const [processedData, setProcessedData] = useState([]);

    useEffect(() => {
        setProcessedData(tempData.division(columnNumber));
    }, []);

    const clickButton = () => {
        console.log("심인용 바보");
        fetch("/students-data").then((res) => {
            console.log(res);
        });
    };

    return (
        <Container style={{ height: "100%" }}>
            <Header />
            <div>
                <SeatTable>
                    {processedData.map((col) => (
                        <div>
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
            <Footer />
        </Container>
    );
}

export default StudentsArr;
