import React, { useState } from "react";
import { Button, Form, Spinner } from "react-bootstrap";
import "./InputColNum.css";


type InputColNumProps = {
    onSubmit: (col:number) => void;
    loading: boolean;
}

function InputColNum({ onSubmit, loading }:InputColNumProps) {
    const MAX_NUMBER = 5;
    const MIN_NUMBER = 1;
    const [number, setNumber] = useState<number>(MIN_NUMBER);
    /*
    const clickUpButton = async () => {
        if (number < MAX_NUMBER) {
            await setNumber(number + 1);
        }
    };

    const clickDownButton = async () => {
        if (number > MIN_NUMBER) {
            await setNumber(number - 1);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(number);
    };

    const handleReset = async () => {
        await setNumber(MIN_NUMBER);
    };
*/
    const tempSubmit = (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        onSubmit(4);
    };

    return (
        <form>
            <div style={{ display: "table", width: "100%" }}>
                <div
                    style={{
                        display: "table-cell",
                        verticalAlign: "middle",
                        height: "400px",
                    }}
                >
                    <div style={{ display: "flex", justifyContent: "center" }}>
                        <div>
                            {loading ? (
                                <Spinner animation="grow" variant="dark" />
                            ) : (
                                <Button
                                    style={{ width: "150px" }}
                                    variant="success"
                                    type="submit"
                                    onClick={tempSubmit}
                                >
                                    Start
                                </Button>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </form>
    );
}

export default InputColNum;
/*
<form>
            <div className="input-wrapper">
                <div className="box">
                    <div className="box-subject">
                        <h2>Input Column Number</h2>
                    </div>
                    <div className="box-main">
                        <div className="box-main__input-wrapper">
                            <input
                                className="box-main__input"
                                value={number}
                                readOnly
                            />
                        </div>
                        <div className="box-main__btn-wrapper">
                            <div className="box-main__btn">
                                <Button variant="dark" onClick={clickUpButton}>
                                    △
                                </Button>
                            </div>
                            <div className="box-main__btn">
                                <Button
                                    variant="dark"
                                    onClick={clickDownButton}
                                >
                                    ▽
                                </Button>
                            </div>
                        </div>
                    </div>
                    <div className="box-submit">
                        <div className="box-submit__btn">
                            <Button
                                className="w-100"
                                variant="success"
                                type="submit"
                                onClick={handleSubmit}
                            >
                                Submit
                            </Button>
                        </div>
                        <div className="box-submit__btn">
                            <Button
                                className="w-100"
                                variant="warning"
                                onClick={handleReset}
                            >
                                Reset
                            </Button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
*/
