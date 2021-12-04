import React, { useState } from "react";
import StudentsArr from "./StudentsArr";
import InputColNum from "./InputColNum";
import ReturnBtn from "../components/ReturnBtn";
import dummyData from "../dummyData";
import "bootstrap/dist/css/bootstrap.min.css";

interface HomeProps {
    match:any;
    location:any;
    history:any;
}

function Home(props:HomeProps) {

    console.log(props.match)
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
        setIsFetching(true);

        const response = await getDatafromServer("/students-data");

        setStudentsData(response);
        setColNum(e);
        setIsInputColNum(true);
    };

    const handleReturnBtnSubmit = () => {
        setIsFetching(false);
        setIsInputColNum(false);
    };

    return (
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
    );
}

export default Home;
