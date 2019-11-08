import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";

import ClipStripe from "./ClipStripe";
import Image from "./Image";

const useStyles = makeStyles(theme => ({
  root: {}
}));

const ClipComponent = ({ clip, clipImages, activeImage }) => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <Image {...activeImage} />
      <ClipStripe images={clipImages} />
    </div>
  );
};

const Clip = connect(
  (state, ownProps) => ({
    clip: state.clips[0],
    clipImages: _.map(
      state.clips.byKey["1"].images,
      id => state.images.byKey[id]
    ),
    activeImage: state.images.byKey["1"]
  }),
  (dispatch, ownProps) => ({})
)(ClipComponent);

export default Clip;
