import React from "react";
import styled from "styled-components";
import Logo from "../../assets/image/Logo.svg";
import { Link } from "react-router-dom";

const TitleArray = [
  {
    id: 1,
    name: "치명률",
    link: "",
  },
  {
    id: 2,
    name: "해외 동향",
    link: "Abroad",
  },
  {
    id: 3,
    name: "주요 질병 치명률",
    link: "MajorDisease",
  },
  {
    id: 4,
    name: "광고 목적",
    link: "Advertisement",
  },
];

export default function Bar() {
  return (
    <BarWrap>
      <LinkWrap to="/">
        <TitleWrap>
          <Img
            style={{ width: "41px", height: "48px" }}
            src={Logo}
            alt="Logo"
          />
          <span style={{ fontWeight: "bold", fontSize: "18px" }}>Fear Not</span>
        </TitleWrap>
      </LinkWrap>
      <MenuWrap>
        {TitleArray.map((menu) => (
          <LinkWrap to={menu.link} key={menu.id}>
            <MenuBtnLabel id="menu" key={menu.id}>
              <InputWrap
                type="radio"
                name="menu"
                value={menu.name}
                id="menu"
              ></InputWrap>
              <ButtonWrap>{menu.name}</ButtonWrap>
            </MenuBtnLabel>
          </LinkWrap>
        ))}
      </MenuWrap>
    </BarWrap>
  );
}

const LinkWrap = styled(Link)`
  text-decoration: none;
  color: #7c7c7c;
`;

const InputWrap = styled.input`
  visibility: hidden;
  appearance: none;
`;

const ButtonWrap = styled.div`
  margin-bottom: 20px;
  background-color: transparent;
  font-size: 15px;
  padding: 13px 19.96px;
  transition: all 0.5s ease 0s;
  cursor: pointer;
  ${InputWrap}:checked + && {
    background-color: black;
    border: none;
  }
  &:hover {
    box-shadow: 0px 3px 15px -5px rgba(0, 0, 0, 0.3);
  }

  /* &:checked {
    background-color: #493e3e;
  }
  ${InputWrap}:checked + && {
    background-color: #493e3e;
    color: white;
  } */
`;

const MenuBtnLabel = styled.label`
  margin: 0 10px;
`;

const MenuWrap = styled.div`
  margin-top: 40px;
`;

const Img = styled.img`
  margin-right: 10px;
`;

const BarWrap = styled.div`
  position: fixed;
  width: 150px;
  height: 100%;
  background-color: #efffe8;
`;
const TitleWrap = styled.div`
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
`;
