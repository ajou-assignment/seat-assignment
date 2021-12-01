import { Button } from "react-bootstrap";



type ReturnBtnProps = {
    onSubmit: (toggle:boolean)=> void;
}

function ReturnBtn ( {onSubmit}:ReturnBtnProps ) {
    const handleSubmit = async (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        await onSubmit(false);
    };

    return (
        <form>
            <div
                style={{
                    padding: "10px",
                    display: "flex",
                    justifyContent: "center",
                }}
            >
                <Button variant="success" type="submit" onClick={handleSubmit}>
                    다시 입력
                </Button>
            </div>
        </form>
    );
}

export default ReturnBtn;
