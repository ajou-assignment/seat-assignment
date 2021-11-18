//import "bootstrap/dist/css/bootstrap.min.css";
import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import Footer from "./components/Footer";
import Header from "./components/Header";
import SeatCell from "./components/SeatCell";
import SeatTable from "./components/SeatTable";
import tempData from "./tempData";
import "./ArrayMethod";

function App() {
    const [colNum, setColNum] = useState(2);
    const [processedData, setProcessedData] = useState([]);

    useEffect(() => {
        fetch("/students-data");
    });

    useEffect(() => {
        setColNum(3);
        setProcessedData(tempData.division(colNum));
    }, []);

    return (
        <Container style={{ height: "100%" }}>
            <Header />
            <SeatTable>
                {processedData.map((col) => (
                    <div>
                        {col.map((duo, index) => (
                            <SeatCell key={index} duo={duo} />
                        ))}
                    </div>
                ))}
            </SeatTable>
            <Footer />
        </Container>
    );
}

export default App;
