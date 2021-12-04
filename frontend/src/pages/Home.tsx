import InputColNum from "../components/InputColNum";
import "bootstrap/dist/css/bootstrap.min.css";
import {useNavigate} from "react-router-dom"


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
        <div style={{minHeight: "550px", width: "100%", display:"table"}}>
            <div style={{width: "100%", display: "table-cell", verticalAlign: "middle"}}>
                <InputColNum onSubmit={handleSubmit} />
            </div>
        </div>
    );
}

export default Home;
