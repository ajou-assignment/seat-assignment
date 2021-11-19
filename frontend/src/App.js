import { useState } from "react";
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import StudentsArr from "./pages/StudentsArr.js";
import InputColNum from "./pages/InputColNum.js";
import ReturnBtn from "./components/ReturnBtn.js";
import tempData from "./tempData.js";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [data, setData] = useState([...tempData]);
    const [colNum, setColNum] = useState(3);
    const [isInputColNum, setIsInputColNum] = useState(false);

    const handleInputColNumSubmit = async (e) => {
        await setColNum(e);
        await setIsInputColNum(true);
    };

    const handleReturnBtnSubmin = async () => {
        await setIsInputColNum(false);
    };

    return (
        <div>
            <Header />
            <div>
                {isInputColNum ? (
                    <div>
                        <StudentsArr
                            studentsData={[...data]}
                            columnNumber={colNum}
                        />
                        <ReturnBtn onSubmit={handleReturnBtnSubmin} />
                    </div>
                ) : (
                    <InputColNum onSubmit={handleInputColNumSubmit} />
                )}
            </div>
            <Footer />
        </div>
    );
}

export default App;
