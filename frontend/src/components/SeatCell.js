import "./SeatCell.css";

function Desks({ leftPerson, rightPerson }) {
    return (
        <div className="desks">
            <div className="desk__left">
                <p className="desk__name">{leftPerson.name}</p>
                <p className="desk__satisfy">
                    만족도 <span className="desk__satisfy--score">33</span>
                </p>
            </div>
            <div className="desk__right">
                <p className="desk__name">{rightPerson.name}</p>
                <p className="desk__satisfy">
                    만족도 <span className="desk__satisfy--score">33</span>
                </p>
            </div>
        </div>
    );
}

function SeatCell({ duo }) {
    const { left } = duo;
    let right = {
        id: left.id + 1,
        name: "None",
    };

    if (duo.right) {
        right = duo.right;
    }

    return <Desks leftPerson={left} rightPerson={right} />;
}

export default SeatCell;
