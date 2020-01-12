import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import {graphql, createFragmentContainer} from 'react-relay'

import GridListTile from "@material-ui/core/GridListTile";
import GridListTileBar from "@material-ui/core/GridListTileBar";
import IconButton from "@material-ui/core/IconButton";
import StarBorderIcon from "@material-ui/icons/StarBorder";

const useStyles = makeStyles(theme => ({
    title: {
      color: theme.palette.primary.light
    },
    titleBar: {
      background:
        "linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)"
    },
    img: {
        width: 'auto',
        height: '200px'
    },
    placeholder: { backgroundColor: "grey", width: "100%", height: "100%" }
  }));



const FramePreview = ({frame, key}) => {
  const classes = useStyles();

  return (
    <GridListTile>
    <img className={classes.img} alt={"title"} src={frame.url} />
    <GridListTileBar
      title={"title"}
      classes={{
        root: classes.titleBar,
        title: classes.title
      }}
      actionIcon={
        <IconButton aria-label={`star fooo`}>
          <StarBorderIcon className={classes.title} />
        </IconButton>
      }
    />
  </GridListTile>
  );
};

export default createFragmentContainer(
    FramePreview,
  // Each key specified in this object will correspond to a prop available to the component
  {
    frame: graphql`
      # As a convention, we name the fragment as '<ComponentFileName>_<propName>'
      fragment FramePreview_frame on Frame {
        url
      }
    `
  },
)
