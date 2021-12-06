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

    return (
        <form>
            <div className="wrapper">
                <div className="input-wrapper">
                    <div>
                        <div className="col-box">
                            <div className="col-box__subject">
                                <p>라인 설정</p>
                            </div>
                            <div className="col-box__main">
                                <div className="test">
                                    <div className="col-box__main--btn">
                                        <Button variant="primary" onClick={clickDownButton}>
                                            ◁
                                        </Button>
                                    </div>
                                    <div className="col-box__main--number">
                                        <p>{number}</p>
                                    </div>
                                    <div className="col-box__main--btn">
                                        <Button
                                            variant="primary"
                                            onClick={clickUpButton}
                                        >
                                            ▷
                                        </Button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="option-box">
                            <div className="option-box__gen-div">
                                <div className="option-box__options">
                                    <input type="checkbox"/>
                                    <p>남녀 구분</p>
                                </div>
                            </div>
                            <div className="option-box__sd-min">
                                <div className="option-box__options">
                                    <input type="checkbox"/>
                                    <p>표준편차 최소화</p>
                                </div>
                            </div>
                        </div>
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
                        Next
                    </Button>
                </div>
            </div>
        </form>
        
    );
}

export default InputColNum;


