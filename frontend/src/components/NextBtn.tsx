import { Button } from "react-bootstrap";
import "./style/NextBtn.css"

interface NextBtn {
    title: string;
    onClick: (e:React.MouseEvent<HTMLButtonElement>) => void;
}


function NextBtn ({title, onClick}:NextBtn) {

    const handleSubmit = (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        onClick(e);
    };

    return (
        <div className="box-submit">
            <div className="box-submit__btn">
                <Button
                    className="w-100"
                    variant="success"
                    type="submit"
                    onClick={handleSubmit}
                >
                    {title}
                </Button>
            </div>
        </div>
    );
};

export default NextBtn