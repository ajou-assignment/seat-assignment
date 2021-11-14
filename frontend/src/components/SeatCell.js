function Person({ person }) {
    return (
        <div
            style={{
                margin: 0,
                display: "flex",
                justifyContent: "center",
                border: "2px solid grey",
            }}
        >
            <h3>{person.id}</h3>
            <h3>{person.name}</h3>
        </div>
    );
}

function SeatCell({ duo }) {
    const { left, right } = duo;
    return (
        <div
            style={{
                margin: "5px",
                display: "flex",
                justifyContent: "center",
            }}
        >
            <Person person={left} />
            <Person person={right} />
        </div>
    );
}

export default SeatCell;
