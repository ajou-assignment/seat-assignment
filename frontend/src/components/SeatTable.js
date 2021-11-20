function SeatTable({ children }) {
    return (
        <div
            style={{
                marginTop: "20px",
                paddingTop: "20px",
                paddingBottom: "20px",
                minHeight: "400px",
                display: "flex",
                justifyContent: "center",
            }}
        >
            {children}
        </div>
    );
}

export default SeatTable;
