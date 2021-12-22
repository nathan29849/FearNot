import React from "react";
import styled from "styled-components";
import Graph from "../Components/Fatality/Graph";
import AgeFatality from "../Components/Fatality/AgeFatality";
import Share from "../Components/Fatality/Share";

export default function Fatality() {
  return (
    <FatalityWrap>
      <Graph />
      <AgeFatality />
      <Share />
    </FatalityWrap>
  );
}

const FatalityWrap = styled.div`
  margin-left: 230px;
  margin-right: 80px;
`;
