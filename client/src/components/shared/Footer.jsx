import React from "react";

const Footer = () => {
  return (
    <div
      style={{
        backgroundColor: "#FFDBA4",
        display: "flex",
        gap: "10px",
        justifyContent: "space-around",
        color: "#607274",
      }}
    >
      <div style={{ display: "flex", flexDirection: "column" }}>
        <div>Contact us?</div>
        <div>Copywrite</div>
      </div>
      <div>It's just a footer get over it!</div>
    </div>
  );
};

export default Footer;
