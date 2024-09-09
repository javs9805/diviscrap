import '../App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Divisas from "./Divisas.jsx";
import Home from './Home.jsx'


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
