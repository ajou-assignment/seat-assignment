import { useState } from "react"
import { Routes, Route } from "react-router";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import ClassView from "./pages/ClassView"

function App() {
    const [colNum, setColNum] = useState<number>(0)
    const baseRoute = "/seat-assignment"

    const handleChange = (e:number) => {
        setColNum(e)
    }

    return (
        <div>
            <Header />
            <Routes>
                <Route path={`${baseRoute}/`} element={<Home onChange={handleChange}/>} />
                <Route path={`${baseRoute}/classview`} element={<ClassView col={colNum}/>} />
            </Routes>
            <Footer />
        </div>
    );
}

export default App;
