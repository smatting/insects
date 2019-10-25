import React from "react";
import ReactDOM from "react-dom";
import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import { createEpicMiddleware } from "redux-observable";
import logger from "redux-logger";

import epics from "./epics";
import reducers from "./reducer";

import { makeStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import AppBar from "@material-ui/core/AppBar";
import CssBaseline from "@material-ui/core/CssBaseline";
import Toolbar from "@material-ui/core/Toolbar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import List from "@material-ui/core/List";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import InboxIcon from "@material-ui/icons/MoveToInbox";
import MailIcon from "@material-ui/icons/Mail";

import ClipOverview from "./container/ClipOverview";
import Clip from "./container/Clip";

const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
  root: {
    display: "flex"
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0
  },
  drawerPaper: {
    width: drawerWidth
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3)
  },
  stripe: {
    backgroundColor: "red"
  },
  toolbar: theme.mixins.toolbar
}));

const Index = ({ view }) => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" noWrap>
            Insect Counter
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper
        }}
      >
        <div className={classes.toolbar} />
        <List>
          <ListItem button key="overview">
            <ListItemText primary="Overview" />
          </ListItem>
        </List>
      </Drawer>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        {/* {view == "OVERVIEW" ? <ClipOverview /> : null} */}
        {view == "CLIP" ? <Clip /> : null}
      </main>
    </div>
  );
};

const epicMiddleware = createEpicMiddleware();

const middlewares = [logger, epicMiddleware];

const enhancer = compose(applyMiddleware(...middlewares));

const initalState = {};

const store = createStore(reducers, initalState, enhancer);

epicMiddleware.run(epics);

const IndexContainer = connect(
  (state, ownProps) => ({ view: state.view }),
  (dispatch, ownProps) => ({
    // onMount: () => dispatch(a.initApp())
  })
)(Index);

ReactDOM.render(
  <Provider store={store}>
    <IndexContainer />
  </Provider>,
  document.getElementById("index")
);
