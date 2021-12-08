import {useNavigate} from "react-router-dom"
import InputSetting from "../components/InputSetting";
import MainContents from "../components/MainContents";
import "bootstrap/dist/css/bootstrap.min.css";
import "./style/Home.css"



interface Data {
    colnum : number;
    genDiv : boolean;
    stdDev : boolean;
    noAgain: boolean;
}

type HomeProps = {
    onChange:(data:Data)=>void
}

function Home({onChange}:HomeProps) {
    const navigate = useNavigate();

    const handleSubmit = async (e:Data) => {
        onChange(e);
        navigate("/seat-assignment/classview")
    };

    return (
        <MainContents title="SET">
            <InputSetting onSubmit={handleSubmit} />
        </MainContents>
    );
}

export default Home;
