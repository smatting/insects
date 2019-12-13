import type {ClipPreview_previewFrame} from './__generated__/ClipPreview_previewFrame.graphql';
import { makeStyles, withStyles } from "@material-ui/core/styles";

import React from 'react';
import {graphql, createFragmentContainer} from 'react-relay'

import GridListTile from "@material-ui/core/GridListTile";
import GridListTileBar from "@material-ui/core/GridListTileBar";
import IconButton from "@material-ui/core/IconButton";
import InfoIcon from "@material-ui/icons/Info";


type Props = {
    previewFrame: ClipPreview_previewFrame
}

const styles = theme => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "space-around",
    overflow: "hidden",
    backgroundColor: theme.palette.background.paper
  },
  gridList: {
    width: "100%"
    // height: 450
  },
  icon: {
    color: "rgba(255, 255, 255, 0.54)"
  }
});


class ClipPreview extends React.Component<Props> {
  render() {
    const classes = this.props.classes;
    const {url, id} = this.props.previewFrame;

    return (
        <GridListTile key={id}>
        <img src={url} alt={"tile.author"} />
        {console.log(url)}
        <GridListTileBar
          title={"test"}
          subtitle={<span>by: {"tile.author"}</span>}
          actionIcon={
            <IconButton aria-label={`info about`} className={classes.icon}>
              <InfoIcon />
            </IconButton>
          }
        />
      </GridListTile>
    );
  }
}

export default createFragmentContainer(
    withStyles(styles)(ClipPreview),
  // Each key specified in this object will correspond to a prop available to the component
  {
    previewFrame: graphql`
      # As a convention, we name the fragment as '<ComponentFileName>_<propName>'
      fragment ClipPreview_previewFrame on Frame {
        url
      }
    `
  },
)


