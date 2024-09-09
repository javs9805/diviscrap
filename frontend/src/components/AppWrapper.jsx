import logo from '../logo.svg';
import '../App.css';
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Header from "./Header.jsx";
import Divisas from "./Divisas.jsx";
import Home from './Home.jsx'
import { Container } from 'lucide-react';


const AppWrapper = () => {
  return (
    <Router>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/maxicambios"element={<Divisas casa="maxicambios" />} />
            <Route path="/cambioschaco"element={<Divisas casa="cambioschaco" />} />
        </Routes>
    </Router>
  );
};

export default AppWrapper;
