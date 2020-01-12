// ViewerTodoList.js
import React from 'react';
import { makeStyles } from "@material-ui/core/styles";

import GridList from "@material-ui/core/GridList";
import GridListTile from "@material-ui/core/GridListTile";
import GridListTileBar from "@material-ui/core/GridListTileBar";
import IconButton from "@material-ui/core/IconButton";
import InfoIcon from "@material-ui/icons/Info";

const useStyles = makeStyles({
    gridList: {
        width: "100%"
    },
    icon: {
        color: "rgba(255, 255, 255, 0.54)"
    },
    img: {
        width: 'auto',
        height: '200px'
    }
}
);


const FrameTile = ({thumbUrl}) => {
    const classes = useStyles();
    return (
    <GridListTile>
    <img src={thumbUrl} alt={"tile.author"} className={classes.img} />
    <GridListTileBar
      title={"test"}
      subtitle={<span>by: {"tile.author"}</span>}
      actionIcon={
        <IconButton aria-label={`info about`} className={classes.icon}>
          <InfoIcon />
        </IconButton>
      }
    />
  </GridListTile>)
}

const FrameGrid = ({frames}) => {
    const classes = useStyles();
    return (
        <GridList cellHeight={180} className={classes.gridList} cols={5}>
        {frames.map((frame, idx) =>
        <FrameTile key={'frame-'+idx} {...frame}/>
        )}
    </GridList>
    )
}

export default FrameGrid;
