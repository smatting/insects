// ViewerTodoList.js
import React from 'react';
import {graphql, QueryRenderer} from 'react-relay';
import { withStyles } from "@material-ui/core/styles";

import Environment from './GraphQLEnvironment'
import FrameGrid from './FrameGrid'

const styles = theme => ({
    root: {
      display: "flex",
      flexWrap: "wrap",
      justifyContent: "space-around",
      overflow: "hidden",
      backgroundColor: theme.palette.background.paper
    }
  });


const getNodes = ({edges}) => _.map(edges,({node}) => node);

class Frames extends React.Component {
  query_render({error, props}) {
        if (error) {
          return <div>Error!</div>;
        }
        if (!props) {
          return <div>Loading...</div>;
        }
        console.log(props)
        return (
        <FrameGrid frames={getNodes(props.allFrames)} />
        );
      }


  render() {
    const classes = this.props.classes;
    return (
      <QueryRenderer
        environment={Environment}
        query={graphql`
        query FramesQuery {
            allFrames(url: "test1") {
              edges {
                node {
                  id
                  url
                  thumbUrl
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

export default withStyles(styles)(Frames)