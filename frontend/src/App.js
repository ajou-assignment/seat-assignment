//import "bootstrap/dist/css/bootstrap.min.css";
import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import Footer from "./components/Footer.js";
import Header from "./components/Header.js";
import SeatCell from "./components/SeatCell.js";
import SeatTable from "./components/SeatTable.js";
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
