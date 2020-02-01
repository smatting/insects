import React from "react";

import { connect } from "react-redux";
import { withStyles } from "@material-ui/core/styles";
import * as a from "../actions";
import FrameGrid from "./FrameGrid";
import BrowserNav from "./BrowserNav";

const styles = theme => ({});

const Browser = ({ search, ntotal, frames, onSearchUpdate }) => {
  return (
    <>
      <BrowserNav search={search} onSearchUpdate={onSearchUpdate} />
      {ntotal ? <div>Total: {ntotal}</div> : <div></div>}
      <FrameGrid frames={frames} />
    </>
  );
};

export default withStyles(styles)(
  connect(
    (state, ownProps) => ({
      search: state.search,
      frames: state.searchResults.frames,
      ntotal: state.searchResults.ntotal
    }),
    (dispatch, ownProps) => ({
      onSearchUpdate: search => dispatch(a.updateSearch(search))
    })
  )(Browser)
);
