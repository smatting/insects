import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import ClipStripe from "./ClipStripe";
import Image from "./Image";

const useStyles = makeStyles(theme => ({
  root: {}
}));

const Sequence = () => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <Image />
      <ClipStripe />
    </div>
  );
};

export default Sequence;
