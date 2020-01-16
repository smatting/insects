import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  img: { width: "auto", height: 600 },
});



const Frame = ({url}) => {
    const classes = useStyles();
    return (<img className={classes.img} src={url} />)
}


  export default Frame;
