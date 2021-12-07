import { useState } from "react"
import { Routes, Route } from "react-router";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ClassView from "./pages/ClassView"
import "./App.css"

function App() {
    const [colNum, setColNum] = useState<number>(0)
    const baseRoute = "/seat-assignment"

    const handleChange = (e:number) => {
        setColNum(e)
    }

    return (
        <div className="app-wrapper">
            <div className="app-container">
                <Routes>
                    <Route path={`${baseRoute}/`} element={<Home onChange={handleChange}/>} />
                    <Route path={`${baseRoute}/classview`} element={<ClassView col={colNum}/>} />
                </Routes>
                <Footer />
            </div>
        </div>
    );
}

export default App;
