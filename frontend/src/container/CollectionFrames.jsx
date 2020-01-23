import React from "react";
import { graphql, QueryRenderer } from "react-relay";
import { withStyles } from "@material-ui/core/styles";

import Environment from "./GraphQLEnvironment";
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
    return <FrameGrid frames={props.frames} />;
  }

  render() {
    const { classes, collectionId } = this.props;
    return (
      <QueryRenderer
        environment={Environment}
        query={graphql`
          query FramesQuery($collectionId: String!) {
            frames(collectionId: $tbegin, tend: $tend, nframes: 10) {
              id
              url
              timestamp
              thumbnail
            }
          }
        `}
        variables={{ collectionId }}
        render={this.query_render.bind(this)}
      />
    );
  }
}

export default withStyles(styles)(Frames);
