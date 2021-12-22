import React from "react";
import styled from "styled-components";
import {
  FacebookShareButton,
  FacebookIcon,
  FacebookMessengerShareButton,
  FacebookMessengerIcon,
  TwitterShareButton,
  TwitterIcon,
  LineShareButton,
  LineIcon,
} from "react-share";
import Banner from "../../assets/image/Banner.svg";
import URLShare from "../../assets/image/Share.svg";
import { CopyToClipboard } from "react-copy-to-clipboard";

export default function Share() {
  const currentUrl = window.location.href;
  return (
    <ShareWrap>
      <TitleWrap>공유하기</TitleWrap>
      <CopyToClipboard text={currentUrl}>
        <ShareButton onClick={() => alert("URL을 복사했습니다.")}>
          <img
            src={URLShare}
            style={{ width: "48px", height: "48px", marginRight: "20px" }}
            alt="URLShare"
          />
        </ShareButton>
      </CopyToClipboard>
      <FacebookShareButton style={{ marginRight: "20px" }} url={currentUrl}>
        <FacebookIcon size={48} round={true} borderRadius={24}></FacebookIcon>
      </FacebookShareButton>
      <FacebookMessengerShareButton
        style={{ marginRight: "20px" }}
        url={currentUrl}
      >
        <FacebookMessengerIcon
          size={48}
          round={true}
          borderRadius={24}
        ></FacebookMessengerIcon>
      </FacebookMessengerShareButton>
      <TwitterShareButton style={{ marginRight: "20px" }} url={currentUrl}>
        <TwitterIcon size={48} round={true} borderRadius={24}></TwitterIcon>
      </TwitterShareButton>
      <LineShareButton url={currentUrl}>
        <LineIcon size={48} round={true} borderRadius={24}></LineIcon>
      </LineShareButton>
      <img
        style={{ display: "block", margin: "30px auto 50px auto" }}
        src={Banner}
        alt="Banner"
      />
    </ShareWrap>
  );
}

const ShareButton = styled.button`
  background-color: transparent;
  border: none;
  cursor: pointer;
`;

const ShareWrap = styled.div`
  grid-template-columns: repeat(4, 48px);
  grid-column-gap: 8px;
  justify-content: center;
  margin-bottom: 16px;
  text-align: center;
`;

const TitleWrap = styled.div`
  text-shadow: 1px 1px 2px grey;
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 40px;
  text-align: center;
`;
