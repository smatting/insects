// ViewerTodoList.js
import React from 'react';
import {graphql, QueryRenderer} from 'react-relay';

import Environment from './GraphQLEnvironment'
import ClipPreview from './ClipPreview'

export default class ClipOverview extends React.Component {
  render() {
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
        render={({error, props}) => {
          if (error) {
            return <div>Error!</div>;
          }
          if (!props) {
            return <div>Loading...</div>;
          }
          return (
            <div>
            {props.allClips.edges.map(edge =>
            <ClipPreview
              key={edge.node.id}
              previewFrame={edge.node.previewFrame}
            />
              )}
            </div>
          );
        }}
      />
    );
  }
}
