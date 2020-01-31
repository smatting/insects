import React from "react";
import styled from "styled-components";

const Container = styled.div`
  border: dashed 2px black;
  box-sizing: border-box;
  transition: box-shadow 0.21s ease-in-out;
`;

function Rectangle(props) {
  const { geometry } = props.annotation;
  if (!geometry) return null;
  return (
    <Container
      className={props.className}
      style={{
        position: "absolute",
        left: `${geometry.x}%`,
        top: `${geometry.y}%`,
        height: `${geometry.height}%`,
        width: `${geometry.width}%`,
        boxShadow: props.active && "0 0 2px 2px yellow inset",
        ...props.style
      }}
    />
  );
}

Rectangle.defaultProps = {
  className: "",
  style: {}
};

export default Rectangle;
