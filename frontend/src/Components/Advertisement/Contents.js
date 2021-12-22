import React from "react";
import styled from "styled-components";
import Banner from "../../assets/image/Banner.svg";

export default function Contents() {
  return (
    <ContentsWrap>
      <TitleWrap>광고 목적</TitleWrap>
      <DescriptionWrap>
        피어낫은 거리두기로 인해 힘들어진 지역상권에 도움이 되기 위해
        시작되었습니다. <br />
        위치기반 서비스로 근처에 있는 소상공인들과 자영업자들의 광고를
        내보냅니다.
        <br /> 광고는 무료 또는 저렴한 가격으로 제공합니다. <br />
        <br />
        피어낫은 지역상권, 소상공인과 지속적으로 공생하기 위해 힘쓰겠습니다.
      </DescriptionWrap>
      <TitleWrap>광고 신청</TitleWrap>
      <DescriptionWrap>
        광고를 원하시는 사업주께서는{" "}
        <a href="mailto:jyhwang118@gmail.com?subject=피어낫 광고 문의 드립니다!">
          여기
        </a>
        로 메일을 보내주세요.
      </DescriptionWrap>
      <TitleWrap>배너 예시</TitleWrap>
      <img style={{ marginTop: "40px" }} src={Banner} alt="Banner" />
    </ContentsWrap>
  );
}

const DescriptionWrap = styled.div`
  margin-top: 68px;
  width: 100%;
`;
const TitleWrap = styled.div`
  margin-top: 40px;
  text-shadow: 1px 1px 2px grey;
  font-weight: bold;
  font-size: 20px;
`;

const ContentsWrap = styled.div`
  margin-left: 230px;
  margin-right: 80px;
`;
