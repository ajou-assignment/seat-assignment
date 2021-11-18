import { useState } from "react";
import StudentsArr from "./pages/StudentsArr";
import InputColNum from "./pages/InputColNum";
import tempData from "./tempData";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [colNum, setColNum] = useState(3);
    const [isInputColNum, setIsInputColNum] = useState(false);

    const handleSubmit = (e) => {
        setColNum(e);
        setIsInputColNum(true);
    };

    return (
        <div>
            {isInputColNum ? (
                <StudentsArr studentsData={tempData} columnNumber={colNum} />
            ) : (
                <InputColNum onSubmit={handleSubmit} />
            )}
        </div>
    );
}

export default App;
