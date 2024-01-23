import React, { Component } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Show from "./MainPage/Show";
import Navbar from "./Navbar";
import ShowStartup from "./Startup/ShowStartup";
import Footer from "./Footer";
import Bid from "./Bidding/Bid";

const App = () => {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        {/* <Route path="/" element={<Show/>}> */}
        <Route index element={<Show />} />
        <Route path="/startup" element={<ShowStartup />} />
        <Route path="/bid" element={<Bid />} />
        {/* </Route> */}
      </Routes>
      <Footer />
    </BrowserRouter>
  );
};

export default App;

ReactDOM.render(<App />, document.getElementById("app"));

{
  /* <a href="/register" class="btn btn-primary">register</a>
        <a href="/startupForm" class="btn btn-primary">startup form</a>
        <a href="/portfolio" class="btn btn-primary">portfolio</a> */
}
//     <div>
//     <h1> react</h1>

//     <Show/>
//     <Newsletter/>
// </div>
