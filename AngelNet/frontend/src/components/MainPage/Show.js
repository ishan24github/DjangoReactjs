import React from "react";

// import Header from "./Header";
import Showcase from "./Showcase";
import Newsletter from "./Newsletter";
import Cards from "./Cards";
import FAQs from "./FAQs";
import Features from "./Features";
// import Form from "../Startup/Form";
import ShowStartup from "../Startup/ShowStartup";

const Show = () => {
  return (
    <div>
      <Showcase />
      <Newsletter/>
      <Features/>
      <Cards />
      <FAQs/>
      {/* <Form/> */}
    </div>
  );
};

export default Show;
