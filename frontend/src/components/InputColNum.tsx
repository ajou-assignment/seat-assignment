import React, { useState } from "react";
import { Button } from "react-bootstrap";
import "./style/InputColNum.css";



interface Data {
    colnum : number;
    genDiv : boolean;
    stdDev : boolean;
}

type InputColNumProps = {
    onSubmit: (data:Data) => void;
}


function InputColNum({ onSubmit }:InputColNumProps) {
    const MAX_NUMBER = 5;
    const MIN_NUMBER = 1;
    //const [number, setNumber] = useState<number>(MIN_NUMBER);
    const [data, setData] = useState<Data>({
        colnum : 1,
        genDiv : false,
        stdDev : false
    })

    const clickUpButton = () => {
        if (data.colnum < MAX_NUMBER) {
            setData(
                {
                    ...data,
                    colnum : data.colnum + 1
                });
        };
    };

    const clickDownButton = () => {
        if (data.colnum > MIN_NUMBER) {
            setData(
                {
                    ...data,
                    colnum : data.colnum - 1
                });
        };
    };

    const handleCheck = (e:React.ChangeEvent<HTMLInputElement>) => {
        const { name, checked } = e.target
        let other:string = ""

        if (name === "genDiv") other = "stdDev";    
        else if (name === "stdDev") other = "genDiv"

        if (checked === true) {
            setData({
                ...data,
                [name] : checked,
                [other] : false
            });
        } else if (checked === false) {
            setData({
                ...data,
                [name] : checked,
            });
        };
    };

    const handleSubmit = (e:React.MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        onSubmit(data);
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
                                        <p>{data.colnum}</p>
                                    </div>
                                    <div className="col-box__main--btn">
                                        <Button variant="primary" onClick={clickUpButton}>
                                            ▷
                                        </Button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="option-box">
                            <div className="option-box__gen-div">
                                <div className="option-box__options">
                                    <input type="checkbox" name="genDiv" checked={data.genDiv} onChange={handleCheck}/>
                                    <p>남녀 구분</p>
                                </div>
                            </div>
                            <div className="option-box__sd-min">
                                <div className="option-box__options">
                                    <input type="checkbox" name="stdDev" checked={data.stdDev} onChange={handleCheck}/>
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


