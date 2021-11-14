import { Container } from "react-bootstrap";

function Header() {
    return (
        <div
            style={{
                paddingTop: "10px",
                display: "flex",
                justifyContent: "center",
            }}
        >
            <div
                style={{
                    width: "60%",
                    border: "3px solid grey",
                    display: "flex",
                    justifyContent: "center",
                }}
            >
                <h2>교 탁</h2>
            </div>
        </div>
    );
}

export default Header;
