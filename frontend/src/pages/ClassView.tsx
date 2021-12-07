import { useEffect, useState } from "react";
import { Spinner } from "react-bootstrap";
import { useNavigate } from "react-router";
import StudentsArr from "../components/StudentsArr";
import ReturnBtn from "../components/ReturnBtn";
import dummyData from "../dummyData";
import Header from "../components/Header";
import "bootstrap/dist/css/bootstrap.min.css";
import "./style/ClassView.css"



interface Data {
    colnum : number;
    genDiv : boolean;
    stdDev : boolean;
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
        
        if (data.genDiv === true) {
            route = baseRoute + "?gen-div=true"
        } else if (data.stdDev === true) {
            route = baseRoute + "?std-dev=true"
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
        <div className="container">
            <p className="title">CLASS</p>
            <div className="content">
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
                                <ReturnBtn onSubmit={handleReturnBtnSubmit} />
                            </div>)
                        }
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ClassView