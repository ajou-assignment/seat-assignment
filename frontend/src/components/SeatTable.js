function SeatTable({ children }) {
    return (
        <div
            style={{
                paddingTop: "20px",
                paddingBottom: "20px",
                display: "flex",
                justifyContent: "center",
            }}
        >
            {children}
        </div>
    );
}

export default SeatTable;
