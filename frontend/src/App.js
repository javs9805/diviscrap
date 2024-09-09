import logo from './logo.svg';
import './App.css';
import Header from "./components/Header.jsx";
import Divisas from "./components/Divisas.jsx";
import Home from './components/Home.jsx'
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";

function App() {
  let routes = useRoutes([
    { path: "/", element: <Home /> },
    { path: "/", element: <Component2 /> },
  ]);
  return routes;
}

const AppWrapper = () => {
  return (
    <App />
  );
};

export default AppWrapper;
