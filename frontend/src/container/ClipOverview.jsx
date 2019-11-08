import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";

import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";
import GridListTileBar from "@material-ui/core/GridListTileBar";
import ListSubheader from "@material-ui/core/ListSubheader";
import IconButton from "@material-ui/core/IconButton";
import InfoIcon from "@material-ui/icons/Info";

const useStyles = makeStyles(theme => ({
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
}));

const makeClips = ({ thumbURL, classes, key }) => (
  <GridListTile key={key}>
    <img src={thumbURL} alt={"tile.author"} />
    {console.log(thumbURL)}
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

const makeGroup = ({ clips, groupName, classes, gidx }) => [
  <GridListTile key={"header" + gidx} cols={5} style={{ height: "auto" }}>
    <ListSubheader component="div">{groupName}</ListSubheader>
  </GridListTile>,
  ..._.map(clips, (clip, cidx) =>
    makeClips({ ...clip, classes, key: "clip-" + cidx + "_" + gidx })
  )
];

const TitlebarGridList = ({ groups }) => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <GridList cellHeight={180} className={classes.gridList} cols={5}>
        {_.map(groups, (group, idx) => makeGroup({ ...group, classes, idx }))}
      </GridList>
    </div>
  );
};

const createGroups = clips =>
  _.map(clips.groupIds, (ids, groupName) => ({
    groupName,
    clips: _.map(ids, id => clips.byKey[id])
  }));

const ClipGroupsContainer = connect(
  (state, ownProps) => ({
    view: state.view,
    groups: createGroups(state.clips)
  }),
  (dispatch, ownProps) => ({})
)(TitlebarGridList);

export default ClipGroupsContainer;
