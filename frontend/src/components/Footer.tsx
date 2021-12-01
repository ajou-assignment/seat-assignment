function Footer() {
    return (
        <div
            style={{
                height: "200px",
                display: "flex",
                justifyContent: "space-around",
                backgroundColor: "#222222",
                color: "#f4f4f4",
            }}
        >
            <div
                style={{
                    display: "table",
                }}
            >
                <h2
                    style={{
                        margin: 0,
                        padding: 0,
                        display: "table-cell",
                        verticalAlign: "middle",
                    }}
                >
                    InyongSim's Output
                </h2>
            </div>
            <div
                style={{
                    display: "table",
                }}
            >
                <ul
                    style={{
                        margin: 0,
                        padding: 0,
                        listStyle: "none",
                        display: "table-cell",
                        verticalAlign: "middle",
                    }}
                >
                    <li>심인용</li>
                    <li>이경민</li>
                    <li>홍성빈</li>
                    <li>정재민</li>
                    <li>정보경</li>
                </ul>
            </div>
        </div>
    );
}

export default Footer;
