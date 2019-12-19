import React from "react";
import { withStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import {graphql, QueryRenderer} from 'react-relay';


import GridList from "@material-ui/core/GridList";

import Frame from "./Frame";
import FramePreview from "./FramePreview";
import Environment from './GraphQLEnvironment'


const styles = theme => ({
    root: {
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-around",
        overflow: "hidden",
        backgroundColor: theme.palette.background.paper
      },
      gridList: {
        flexWrap: "nowrap",
        // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
        transform: "translateZ(0)"
      },
});


class Clip extends React.Component {
    query_render({error, props}) {
        console.log(props)
          if (error) {
            return <div>Error!</div>;
          }
          if (!props) {
            return <div>Loading...</div>;
          }
          return (
            <div className={this.props.classes.root}>
            <Frame frameId={this.props.activeFrame} />
            <div className={this.props.classes.root}>
              <GridList className={this.props.classes.gridList} cols={2.5}>
              {props.clip.frames.edges.map(edge =>
                  <FramePreview
                  key={edge.node.id}
                  frame={edge.node}
                  />
                  )}
              </GridList>
            </div>
          </div>
          );
        }


    render() {
      const classes = this.props.classes;
      return (
        <QueryRenderer
          environment={Environment}
          query={graphql`
          query ClipQuery {
            clip(id: "Q2xpcDoyODQ4") {
              frames {
                edges {
                  node {
                      id
                    ...FramePreview_frame
                  }
                }
              }
            }
          }
          `}
          variables={{}}
          render={this.query_render.bind(this)}
        />
      );
    }
  }


export default connect(
  (state, ownProps) => ({
    activeFrame: "RnJhbWU6MjM1NjU5"
  }),
  (dispatch, ownProps) => ({})
)(withStyles(styles)(Clip));

