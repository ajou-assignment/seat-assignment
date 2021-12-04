import { Routes, Route } from "react-router";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";

function App() {
    return (
        <div>
            <Header />
            <Routes>
                <Route path="/seat-assignment" element={<Home />} />
            </Routes>
            <Footer />
        </div>
    );
}

export default App;
