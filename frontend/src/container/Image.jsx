import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
  //   root: { width: 300, heigth: 500 },
  img: { width: 500, height: 400 }
}));

const Image = () => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <img className={classes.img} src="https://picsum.photos/200/300" />
    </div>
  );
};

export default Image;
