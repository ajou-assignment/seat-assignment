import { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import StudentsArr from "./pages/StudentsArr";
import InputColNum from "./pages/InputColNum";
import ReturnBtn from "./components/ReturnBtn";
import dummyData from "./dummyData";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [colNum, setColNum] = useState<number>(3);
    const [studentsData, setStudentsData] = useState<Array<Array<object>>>([]);
    const [isInputColNum, setIsInputColNum] = useState<boolean>(false);
    const [isFetching, setIsFetching] = useState<boolean>(false);

    const getDatafromServer = async (route:string) => {
        const response = await fetch(route).then((res) => {
            if (res.status === 500) {
                return dummyData;
            }
            return res.json();
        });

        return response;
    };

    const handleInputColNumSubmit = async (e:number) => {
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
