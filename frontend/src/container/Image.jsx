import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  //   root: { width: 300, heigth: 500 },
  img: { width: 500, height: 400 },
  placeholder: { width: 500, height: 400, backgroundColor: "grey" }
}));

const Image = ({ url }) => {
  const classes = useStyles();
  console.log(url);
  return (
    <div className={classes.root}>
      {url ? (
        <img className={classes.img} src={url} />
      ) : (
        <div className={classes.placeholder}></div>
      )}
    </div>
  );
};

export default Image;
