import React, { useState } from "react";
import { Button } from "react-bootstrap";
import "./style/InputColNum.css";


type InputColNumProps = {
    onSubmit: (col:number) => void;
}

function InputColNum({ onSubmit }:InputColNumProps) {
    const MAX_NUMBER = 5;
    const MIN_NUMBER = 1;
    const [number, setNumber] = useState<number>(MIN_NUMBER);

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

    const handleSubmit = (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        onSubmit(number);
    };

    const handleReset = async () => {
        await setNumber(MIN_NUMBER);
    };

    return (
        <form>
            <div className="input-wrapper">
                <div className="box">
                    <div className="box-subject">
                        <h3>How many lines do you want?</h3>
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
        
    );
}

export default InputColNum;


