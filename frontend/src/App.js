//import "bootstrap/dist/css/bootstrap.min.css";
import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import Footer from "./components/Footer";
import Header from "./components/Header";
import SeatCell from "./components/SeatCell";
import SeatTable from "./components/SeatTable";
import tempData from "./tempData.js";

function App() {
    useEffect(() => {
        console.log(tempData);
        return;
    }, []);
    return (
        <Container style={{ height: "100%" }}>
            <Header />
            <SeatTable>
                {tempData.map((duo, index) => (
                    <SeatCell key={index} duo={duo} />
                ))}
            </SeatTable>
            <Footer />
        </Container>
    );
}

export default App;
