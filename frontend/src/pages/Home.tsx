import InputColNum from "../components/InputColNum";
import {useNavigate} from "react-router-dom"
import "bootstrap/dist/css/bootstrap.min.css";
import "./style/Home.css"


type HomeProps = {
    onChange:(col:number)=>void
}

function Home({onChange}:HomeProps) {
    const navigate = useNavigate();

    const handleSubmit = async (e:number) => {
        onChange(e);
        navigate("/seat-assignment/classview")
    };

    return (
        <div className="container">
            <p className="title">SET</p>
            <div className="content">
                <InputColNum onSubmit={handleSubmit} />
            </div>
        </div>
    );
}

export default Home;
