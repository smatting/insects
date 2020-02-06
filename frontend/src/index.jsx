import React from "react";
import ReactDOM from "react-dom";
import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import { createEpicMiddleware } from "redux-observable";
import logger from "redux-logger";

import epics from "./epics";
import reducers from "./reducer";
import * as a from "./actions";

import createSocketIoMiddleware from "redux-socket.io";
import io from "socket.io-client";

import { makeStyles } from "@material-ui/core/styles";
import Drawer from "@material-ui/core/Drawer";
import AppBar from "@material-ui/core/AppBar";
import CssBaseline from "@material-ui/core/CssBaseline";
import Toolbar from "@material-ui/core/Toolbar";
import List from "@material-ui/core/List";
import Typography from "@material-ui/core/Typography";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";

import Browser from "./container/Browser";
import Frame from "./container/Frame";
import LiveView from "./container/LiveView";
import Dataset from "./container/Dataset";

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
  toolbar: theme.mixins.toolbar,
  //   taps: theme.mixins.tabs,
  tabs: {
    backgroundColor: theme.palette.background.paper,
    color: "black",
    minHeight: "48px"
  },
  tabsPlaceholder: {
    minHeight: "48px"
  }
}));

const views = [
  { screenName: "Live", id: "LIVE" },
  { screenName: "Browser", id: "BROWSER" },
  //   { screenName: "Single Dataset", id: "DATASET" },
  { screenName: "Single Frame", id: "FRAME" }
];

const Index = ({ view, updateView }) => {
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
        <Tabs
          className={classes.tabs}
          value={view}
          onChange={(e, view) => updateView(view)}
        >
          {views.map((view, idx) => (
            <Tab
              label={view.screenName}
              value={view.id}
              key={"tab-" + idx}
              id={view.id}
            />
          ))}
        </Tabs>
      </AppBar>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        <div className={classes.tabsPlaceholder} />
        {view == "BROWSER" ? <Browser /> : null}
        {view == "FRAME" ? <Frame /> : null}
        {view == "DATASET" ? <Dataset /> : null}
        {view == "LIVE" ? <LiveView /> : null}
      </main>
    </div>
  );
};

const epicMiddleware = createEpicMiddleware();

let socket = io(process.env.APP_HOST);
let socketIoMiddleware = createSocketIoMiddleware(
  socket,
  (type, action) => action.server
);

const middlewares = [epicMiddleware, socketIoMiddleware, logger];

const enhancer = compose(applyMiddleware(...middlewares));

const initalState = {};

const store = createStore(reducers, initalState, enhancer);

epicMiddleware.run(epics);

const IndexContainer = connect(
  (state, ownProps) => ({ view: state.view }),
  (dispatch, ownProps) => ({
    // onMount: () => dispatch(a.initApp()),
    updateView: view => dispatch(a.updateView(view))
  })
)(Index);

ReactDOM.render(
  <Provider store={store}>
    <IndexContainer />
  </Provider>,
  document.getElementById("index")
);
