import { useState } from "react";
import StudentsArr from "./pages/StudentsArr";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [colNum, setColNum] = useState(3);

    return <StudentsArr columnNumber={2} />;
}

export default App;
