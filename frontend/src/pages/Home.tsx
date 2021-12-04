import { useState } from "react";
import { Spinner } from "react-bootstrap";
import StudentsArr from "../components/StudentsArr";
import InputColNum from "../components/InputColNum";
import ReturnBtn from "../components/ReturnBtn";
import dummyData from "../dummyData";
import "bootstrap/dist/css/bootstrap.min.css";

function Home() {
    const [colNum, setColNum] = useState<number>(3);
    const [studentsData, setStudentsData] = useState<Array<Array<object>>>([]);
    const [isInputColNum, setIsInputColNum] = useState<boolean>(false);
    const [isFetching, setIsFetching] = useState<boolean>(true);

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
        setIsInputColNum(true);

        const response = await getDatafromServer("/students-data");

        setStudentsData(response);
        setColNum(e);
        setIsFetching(false);
    };

    const handleReturnBtnSubmit = () => {
        setIsFetching(false);
        setIsInputColNum(false);
    };
//<Spinner animation="grow" variant="dark" />
    return (
        <div>
            {isInputColNum ? (
                <div>
                    {
                        isFetching ? 
                        ( <Spinner animation="grow" variant="dark" />
                        ) : (
                        <div>
                            <StudentsArr
                                studentsData={[...studentsData]}
                                columnNumber={colNum}
                            />
                            <ReturnBtn onSubmit={handleReturnBtnSubmit} />
                        </div>)
                    }
                </div>
            ) : (
                <InputColNum
                    onSubmit={handleInputColNumSubmit}
                />
            )}
        </div>
    );
}

export default Home;
