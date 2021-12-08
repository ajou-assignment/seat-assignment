import { useState } from "react"
import { Routes, Route } from "react-router";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ClassView from "./pages/ClassView"
import "./App.css"



interface Data {
    colnum : number;
    genDiv : boolean;
    stdDev : boolean;
    noAgain: boolean;
}

function App() {
    const [data, setData] = useState<Data>({
        colnum: 0,
        genDiv: false,
        stdDev: false,
        noAgain: false,
    })
    const baseRoute = "/seat-assignment"

    const handleChange = (e:Data) => {
        setData(e)
    }

    return (
        <div className="app-wrapper">
            <div className="app-container">
                <Routes>
                    <Route path={`${baseRoute}/`} element={<Home onChange={handleChange}/>} />
                    <Route path={`${baseRoute}/classview`} element={<ClassView data={data}/>} />
                </Routes>
                <Footer />
            </div>
        </div>
    );
}

export default App;
