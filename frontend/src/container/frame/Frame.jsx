import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";

import * as a from "../../actions";

import Grid from "@material-ui/core/Grid";

import ImageCard from "./ImageCard";
import LabelList from "./LabelList";

import _ from "lodash";

const useStyles = makeStyles({
  img: { height: "100%" },
  labelsControl: {},
  labelListTable: {}
});

const Frame = ({
  labels,
  frame,
  appearances,
  activeCollection,
  activeFrame,
  onChangeFrame,
  onAddAppearance,
  onDeleteAppearance
}) => {
  console.log(labels);
  if (!frame) {
    return null;
  }

  const classes = useStyles();
  const [activelabels, setActivelabels] = React.useState([labels.allIds[0]]);
  const [activeAnnotation, setActiveAnnotation] = React.useState();

  //   const onChangeActive = id => {
  //     setActiveAnnotation(id);
  //   };

  const handleToggleLabels = value => () => {
    const currentIndex = activelabels.indexOf(value);
    const newActivelabels = [...activelabels];

    if (currentIndex === -1) {
      newActivelabels.push(value);
    } else {
      newActivelabels.splice(currentIndex, 1);
    }

    setActivelabels(newActivelabels);
  };

  //   const onlabelsChange = (e, id) => {
  //     setActivelabels(id);
  //   };

  return (
    <Grid container justify="space-between" spacing={1} alignItems="flex-start">
      <Grid container item xs={9} spacing={1}>
        <ImageCard
          {...{
            activeCollection,
            activelabels,
            activeAnnotation,
            onAddAppearance: appearance =>
              onAddAppearance(frame.id, appearance, activelabels),
            appearances,
            frame,
            onChangeFrame
          }}
        />
      </Grid>
      <Grid container item xs={3} spacing={1}>
        <Grid container item xs={12} spacing={1}>
          <LabelList
            handleToggle={handleToggleLabels}
            labels={labels}
            activelabels={activelabels}
          />
        </Grid>
        <Grid container item xs={12} spacing={1}>
          {/* <LabelList
            classes={classes}
            appearances={appearances}
            labels={labels}
            activeId={activeAnnotation}
            onDelete={onDeleteAppearance}
            onActive={onActive}
          /> */}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default connect(
  (state, ownProps) => ({
    activeCollection: state.activeCollection,
    activeFrame: state.activeFrame,
    frame: state.frames.byKey[state.ui.activeFrame],
    labels: state.labels,
    appearances: state.appearances
  }),
  (dispatch, ownProps) => ({
    onChangeFrame: step =>
      dispatch(a.changeFrame(state.activeCollection, state.activeFrame, step)),
    onAddAppearance: (frameId, appearance, labelIds) =>
      dispatch(a.addAppearance({ frameId, appearance, labelIds })),
    onDeleteAppearance: id => dispatch(a.deleteAppearance(id))
  })
)(Frame);
