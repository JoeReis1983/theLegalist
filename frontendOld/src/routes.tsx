import { Routes, Route } from "react-router-dom";
import AuthPage from './components/AuthPage';
import  About from './components/About';
import MainPage from "./components/MainPage";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="" element={<AuthPage />} />
      <Route path="/about" element={<About />} />
      <Route path="/main" element={<MainPage />} />
    </Routes>
  );
};

export default AppRoutes;