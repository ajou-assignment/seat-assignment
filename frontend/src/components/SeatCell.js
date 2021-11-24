import "./SeatCell.css";

function Desks({ leftPerson, rightPerson }) {
    return (
        <div className="desks">
            <div className="desk__left">
                <p className="desk__name">{leftPerson.name}</p>
                <p className="desk__satisfy">
                    만족도
                    <span className="desk__satisfy--score">
                        {leftPerson.rating}
                    </span>
                </p>
            </div>
            <div className="desk__right">
                <p className="desk__name">{rightPerson.name}</p>
                <p className="desk__satisfy">
                    만족도
                    <span className="desk__satisfy--score">
                        {rightPerson.rating}
                    </span>
                </p>
            </div>
        </div>
    );
}

function SeatCell({ duo }) {
    const { student1 } = duo;
    let student2 = {
        id: student1.id + 1,
        name: "None",
        rating: 0,
    };

    if (duo.student2) {
        student2 = duo.student2;
    }

    return <Desks leftPerson={student1} rightPerson={student2} />;
}

export default SeatCell;
