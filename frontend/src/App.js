import { useState } from "react";
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import StudentsArr from "./pages/StudentsArr.js";
import InputColNum from "./pages/InputColNum.js";
import ReturnBtn from "./components/ReturnBtn.js";
import dummyData from "./dummyData.js";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [colNum, setColNum] = useState(3);
    const [studentsData, setStudentsData] = useState([]);
    const [isInputColNum, setIsInputColNum] = useState(false);
    const [isFetching, setIsFetching] = useState(false);

    const getDatafromServer = async (route) => {
        const response = await fetch(route).then((res) => {
            if (res.status === 500) {
                return dummyData;
            }
            return res;
        });

        return response;
    };

    const handleInputColNumSubmit = async (e) => {
        await setIsFetching(true);

        const response = await getDatafromServer("/students-data");

        await setStudentsData(response);
        await setColNum(e);
        await setIsInputColNum(true);
    };

    const handleReturnBtnSubmit = async () => {
        await setIsFetching(false);
        await setIsInputColNum(false);
    };

    return (
        <div>
            <Header />
            <div>
                {isInputColNum ? (
                    <div>
                        <StudentsArr
                            studentsData={[...studentsData]}
                            columnNumber={colNum}
                        />
                        <ReturnBtn onSubmit={handleReturnBtnSubmit} />
                    </div>
                ) : (
                    <InputColNum
                        onSubmit={handleInputColNumSubmit}
                        loading={isFetching}
                    />
                )}
            </div>
            <Footer />
        </div>
    );
}

export default App;
