import React from "react";
import { Route } from "react-router-dom";
import Fatality from "./Pages/Fatality";
import Abroad from "./Pages/Abroad";
import MajorDisease from "./Pages/MajorDisease";
import Advertisement from "./Pages/Advertisement";
import "./App.css";
import Bar from "./Components/Common/Bar";
import styled from "styled-components";

export default function App() {
  return (
    <AppWrap>
      <Bar />
      <Route exact path="/" component={Fatality} />
      <Route path="/Abroad" component={Abroad} />
      <Route path="/MajorDisease" component={MajorDisease} />
      <Route path="/Advertisement" component={Advertisement} />
    </AppWrap>
  );
}

const AppWrap = styled.div`
  width: 1000px;
  display: flex;
  height: 1118px;
`;
