import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import ListItemText from "@material-ui/core/ListItemText";
import Checkbox from "@material-ui/core/Checkbox";
import IconButton from "@material-ui/core/IconButton";
import CommentIcon from "@material-ui/icons/Comment";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    // maxWidth: 360,
    backgroundColor: theme.palette.background.paper
  }
}));

const LabelList = ({ labels, activelabels, handleToggle }) => {
  const classes = useStyles();

  return (
    <List className={classes.root}>
      {labels.allIds.map(id => {
        const { name, scientificName, systematicLevel } = labels.byKey[id];
        const labelId = `checkbox-list-label-${id}`;

        return (
          <ListItem
            key={id}
            role={undefined}
            dense
            button
            onClick={handleToggle(id)}
          >
            <ListItemIcon>
              <Checkbox
                edge="start"
                checked={activelabels.indexOf(id) !== -1}
                tabIndex={-1}
                disableRipple
                inputProps={{ "aria-labelledby": labelId }}
              />
            </ListItemIcon>
            <ListItemText
              id={labelId}
              primary={name}
              secondary={
                <React.Fragment>
                  <Typography
                    component="span"
                    variant="body2"
                    className={classes.inline}
                    color="textPrimary"
                  >
                    {scientificName}
                  </Typography>
                  {` — ${systematicLevel}`}
                </React.Fragment>
              }
            />
          </ListItem>
        );
      })}
    </List>
  );
};

export default LabelList;
