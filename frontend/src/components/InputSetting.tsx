import React, { useEffect, useState } from "react";
import { Button } from "react-bootstrap";
import "./style/InputSetting.css";



interface Data {
    colnum : number;
    stdDev : boolean;
    noAgain: boolean;
}

type InputColNumProps = {
    onSubmit: (data:Data) => void;
}


function InputColNum({ onSubmit }:InputColNumProps) {
    const MAX_NUMBER = 5;
    const MIN_NUMBER = 1;

    const [data, setData] = useState<Data>({
        colnum : 3,
        stdDev : false,
        noAgain: false,
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
        let options:Array<string> = ["stdDev", "noAgain"]
        const optionIndex = options.indexOf(name)

        if (optionIndex > -1) options.splice(optionIndex, 1)

        if (checked === true) {
            setData({
                ...data,
                [name] : checked,
                [options[0]] : false,
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
                    <div className="settingbox__wrapper">
                        <div className="settingbox">
                            <div className="col-box">
                                <div className="subject">
                                    <p>라인 설정</p>
                                </div>
                                <div className="col-box__main">
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
                            <div className="option-box">
                                <div className="option-box__sd-min">
                                    <div className="option-box__options">
                                        <input type="checkbox" name="stdDev" checked={data.stdDev} onChange={handleCheck}/>
                                        <p>표준편차 최소화</p>
                                    </div>
                                </div>
                                <div className="option-box__no-again">
                                    <div className="option-box__options">
                                        <input type="checkbox" name="noAgain" checked={data.noAgain} onChange={handleCheck}/>
                                        <p>전 짝꿍 피하기</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="filebox">
                        <div className="file-box">
                            <div className="subject">
                                <p>파일 첨부</p>
                            </div>
                            <div className="file-box__main">
                                <div className="file-box__input">
                                    <input type="file" placeholder="dd"/>
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


