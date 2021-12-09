import { useEffect, useState } from "react";
import { Spinner } from "react-bootstrap";
import { useNavigate } from "react-router";
import MainContents from "../components/MainContents"; 
import StudentsArr from "../components/StudentsArr";
import dummyData from "../dummyData";
import Header from "../components/Header";
import "bootstrap/dist/css/bootstrap.min.css";
import "./style/ClassView.css"
import NextBtn from "../components/NextBtn";



interface Data {
    colnum : number;
    stdDev : boolean;
    noAgain: boolean;
}

type ClassViewProps = {
    data:Data
}

function ClassView({ data }:ClassViewProps){
    const [studentsData, setStudentsData] = useState<Array<Array<object>>>([]);
    const [isFetching, setIsFetching] = useState<boolean>(true);

    const navigate = useNavigate()


    const getStudentsData = async (route:string) => {
        const response = await fetch(route).then((res) => {
            if (res.status === 500) {
                return dummyData;
            }
            return res.json();
        });
        return response;
    };

    const handleStudentsData = async () => {
        setIsFetching(true);
        
        const baseRoute = "/students-data"
        let route:string = ""
        
        if (data.stdDev === true) {
            route = baseRoute + "?std-dev=true"
        } else if (data.noAgain === true) {
            route = baseRoute + "?no-again=true"
        } else {
            route = baseRoute
        }
        console.log(route)

        if (data.colnum > 0) {
            const response = await getStudentsData(route);
            setStudentsData(response);
            
        } else {
            navigate("/seat-assignment")
        }
        setIsFetching(false);
    };

    const handleReturnBtnSubmit = () => {
        setIsFetching(false);
        navigate("/seat-assignment")
    };

    useEffect(()=>{
        handleStudentsData()
    }, [])

    return(
        <MainContents title="CLASS">
                <div style={{width:"100%"}}>
                    <Header />
                    <div style={{minHeight: "550px"}}>
                        { isFetching ? 
                            ( 
                                <div style={{minHeight: "550px", width: "100%", display:"table"}}>
                                    <div style={{width: "100%", display: "table-cell", verticalAlign: "middle", textAlign: "center"}}>
                                        <Spinner animation="grow" variant="dark" />
                                    </div>
                                </div>
                            ) : (
                            <div>
                                <StudentsArr studentsData={[...studentsData]} columnNumber={data.colnum} />
                                <NextBtn title="Back" onClick={handleReturnBtnSubmit}/>
                            </div>)
                        }
                    </div>
                </div>
        </MainContents>
    );
}

export default ClassView