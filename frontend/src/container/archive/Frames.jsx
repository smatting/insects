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

const getNodes = ({ edges }) => _.map(edges, ({ node }) => node);

class Frames extends React.Component {
  query_render({ error, props }) {
    if (error) {
      return <div>Error!</div>;
    }
    if (!props) {
      return <div>Loading...</div>;
    }
    console.log("Frames props", props);
    return <FrameGrid frames={props.frames} showSelect={false} />;
  }

  render() {
    const classes = this.props.classes;
    /*
    return (
      <QueryRenderer
        environment={Environment}
        query={graphql`
          query FramesQuery($tbegin: DateTime!, $tend: DateTime!) {
            frames(tbegin: $tbegin, tend: $tend, nframes: 10) {
              id
              url
              timestamp
              thumbnail
            }
          }
        `}
        variables={{ tbegin: this.props.startDate, tend: this.props.endDate }}
        render={this.query_render.bind(this)}
      />
    );
    */
  }
}

export default withStyles(styles)(Frames);
