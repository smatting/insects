// ViewerTodoList.js
import React from 'react';
import {graphql, QueryRenderer} from 'react-relay';
import { withStyles } from "@material-ui/core/styles";

import GridList from "@material-ui/core/GridList";
import Environment from './GraphQLEnvironment'
import ClipPreview from './ClipPreview'

const styles = theme => ({
    root: {
      display: "flex",
      flexWrap: "wrap",
      justifyContent: "space-around",
      overflow: "hidden",
      backgroundColor: theme.palette.background.paper
    },
    gridList: {
      width: "100%"
    },
    icon: {
      color: "rgba(255, 255, 255, 0.54)"
    }
  });


class ClipOverview extends React.Component {
  query_render({error, props}) {
        if (error) {
          return <div>Error!</div>;
        }
        if (!props) {
          return <div>Loading...</div>;
        }
        return (
          <div>
              <GridList cellHeight={180} className={this.props.classes.gridList} cols={5}>
                  {props.allClips.edges.map(edge =>
                  <ClipPreview
                  key={edge.node.id}
                  previewFrame={edge.node.previewFrame}
                  />
                  )}
            </GridList>
          </div>
        );
      }


  render() {
    const classes = this.props.classes;
    return (
      <QueryRenderer
        environment={Environment}
        query={graphql`
        query ClipOverviewQuery {
            allClips(first: 20) {
              edges {
                node {
                  id
                  previewFrame {
                    ...ClipPreview_previewFrame
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

export default withStyles(styles)(ClipOverview)
