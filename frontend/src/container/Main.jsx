import React from "react";
import _ from "lodash";
import * as a from "../actions";
import { connect } from "react-redux";
import { withStyles } from "@material-ui/core/styles";

const styles = theme => ({
  root: {

  },
});

class Component extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    const { classes } = this.props;
    return (
    );
  }
}


const Component = withStyles(styles)(
  connect(
    (state, ownProps) => ({
    }),
    (dispatch, ownProps) => ({
    })
  )(Container)
);

export { Container };
