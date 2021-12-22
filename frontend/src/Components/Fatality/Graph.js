import React, { useState, useEffect } from "react";
import styled from "styled-components";
import axios from "axios";
import Banner from "../../assets/image/Banner.svg";
import MyResponsiveLine from "./MyResponsiveLine";

const dataArray = [
  {
    id: "norway",
    color: "hsl(311, 70%, 50%)",
    data: [
      {
        x: "11/1",
        y: 0.83,
      },
      {
        x: "11/2",
        y: 0.84,
      },
      {
        x: "11/3",
        y: 0.78,
      },
      {
        x: "11/4",
        y: 0.81,
      },
      {
        x: "11/5",
        y: 0.81,
      },
      {
        x: "11/6",
        y: 0.8,
      },
      {
        x: "11/7",
        y: 0.75,
      },
      {
        x: "11/8",
        y: 0.72,
      },
      {
        x: "11/9",
        y: 0.74,
      },
      {
        x: "11/10",
        y: 0.71,
      },
      {
        x: "11/11",
        y: 0.74,
      },
      {
        x: "11/12",
        y: 0.75,
      },
    ],
  },
];

export default function Graph() {
  const [facilityData, setFacilityData] = useState([]);
  useEffect(() => {
    const url = "/api/corona/20211101/20211112/";
    axios
      .get(url, {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Credentials": true,
        },
      })
      .then((res) => {
        console.log(res.data);
        setFacilityData(res.data);
        console.log(facilityData);
      })
      .catch((err) => console.error(err))
      .finally(() => console.log(facilityData));
  }, []);

  return (
    <GraphWrap>
      <TitleWrap>치명률</TitleWrap>
      <div style={{ height: 300, width: 850 }}>
        <MyResponsiveLine data={dataArray} />
      </div>
      <img
        style={{ display: "block", margin: "30px auto 50px auto" }}
        src={Banner}
        alt="Banner"
      />
    </GraphWrap>
  );
}

const GraphWrap = styled.div`
  margin-top: 40px;
`;

const TitleWrap = styled.div`
  text-shadow: 1px 1px 2px grey;
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 30px;
`;
