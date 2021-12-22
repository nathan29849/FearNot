import React from "react";
import styled from "styled-components";
import GoodMark from "../../assets/image/GoodMark.svg";
import BadMark from "../../assets/image/BadMark.svg";

function getToday() {
  var date = new Date();
  var year = date.getFullYear();
  var month = ("0" + (1 + date.getMonth())).slice(-2);
  var day = ("0" + date.getDate()).slice(-2);

  return year + month + day;
}

export default function AgeFatality() {
  return (
    <AgeFatalityWrap>
      <TitleWrap>연령대 별 치명률: 20211112</TitleWrap>
      <StatisticsWrap>
        <GraphicWrap>
          <div style={{ fontSize: "25px" }}>~30대</div>
          <img
            style={{ width: "130px", margin: "0 50px" }}
            src={GoodMark}
            alt="GoodMark"
          />
          <div style={{ fontSize: "25px" }}>좋음(0.02)</div>
        </GraphicWrap>
        <GraphicWrap>
          <div style={{ fontSize: "25px" }}>40대~60대</div>
          <img
            style={{ width: "130px", margin: "0 50px" }}
            src={GoodMark}
            alt="GoodMark"
          />
          <div style={{ fontSize: "25px" }}>좋음(0.64)</div>
        </GraphicWrap>
        <GraphicWrap>
          <div style={{ fontSize: "25px" }}>60대 이후</div>
          <img
            style={{ width: "130px", margin: "0 50px 5px 50px" }}
            src={BadMark}
            alt="BadMark"
          />
          <div style={{ fontSize: "25px" }}>나쁨(7.94)</div>
        </GraphicWrap>
      </StatisticsWrap>
      <TitleWrap>치명률 계산 과정</TitleWrap>
      <DescriptionWrap>
        치명률이란 그 질병이 얼마나 위험한지를 알 수 있는 지표입니다. 질병에
        걸린 사람 대비 얼마나 많은 사망자가 그 질병으로 인해 사망했는지를 통해
        도출합니다. 위드 코로나 시기에서 가장 중요한 지표는 치명률입니다. 그런데
        현재 제공되는 치명률은 그 가치가 작다고 볼 수 있습니다. 코로나
        바이러스는 변이에 따라 그 치명률이 빠르게 변화하는데에 반해 우리가 보고
        있는 치명률은 코로나 팬데믹 시작부터 지금까지의 정보를 모두 계산하기
        때문입니다. 그래서 "지금 코로나가 얼마나 위험한가?"에 대한 질문에 답을
        내리기가 어렵죠. 코로나 바이러스로 사망하는 사례들을 종합한 결과 감염과
        사망 사이 평균적으로 15일이 걸립니다. 피어낫은 이러한 정보를 이용, 오늘
        기준으로 지난 15일동안의 확진자와 사망자의 정보만을 이용해 "오늘의
        치명률" 정보를 제공합니다. 이를 통해 보다 코로나 바이러스에 대한
        건강하고 과학적인 대처를 할 수 있을 것으로 기대합니다.
      </DescriptionWrap>
    </AgeFatalityWrap>
  );
}

const GraphicWrap = styled.div`
  text-align: center;
`;

const DescriptionWrap = styled.div`
  width: 100%;
`;
const StatisticsWrap = styled.div`
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
`;
const AgeFatalityWrap = styled.div`
  margin-bottom: 40px;
`;

const TitleWrap = styled.div`
  text-shadow: 1px 1px 2px grey;
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 30px;
`;
