import React from "react";
import { withStyles } from "@material-ui/core/styles";

import FrameGrid from "./FrameGrid";

const styles = theme => ({
  root: {
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "space-around",
    overflow: "hidden",
    backgroundColor: theme.palette.background.paper
  }
});

class Dataset extends React.Component {
  query_render({ error, props }) {
    if (error) {
      return <div>Error!</div>;
    }
    if (!props) {
      return <div>Loading...</div>;
    }
    console.log("Frames props", props);
    return <FrameGrid frames={props.frames} showSelect={true} />;
  }

  render() {
    const classes = this.props.classes;
    /*
    return (
      // just a dummy query to have some data
      <QueryRenderer
        environment={Environment}
        query={graphql`
          query DatasetQuery($tbegin: DateTime!, $tend: DateTime!) {
            frames(tbegin: $tbegin, tend: $tend, nframes: 10) {
              id
              url
              timestamp
              thumbnail
            }
          }
        `}
        variables={{
          tbegin: "2019-10-01T00:00:00",
          tend: "2019-12-31T00:00:00"
        }}
        render={this.query_render.bind(this)}
      />
    );
    */
  }
}

export default withStyles(styles)(Dataset);
