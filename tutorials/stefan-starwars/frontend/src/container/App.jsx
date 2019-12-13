import React from "react";
import ReactDOM from "react-dom";
import ShipComponent from './ShipComponent.jsx';

import {
  Environment,
  Network,
  RecordSource,
  Store,
} from 'relay-runtime';

import {graphql, QueryRenderer} from 'react-relay';


function fetchQuery(
  operation,
  variables,
) {
    return fetch('http://0.0.0.0:5000/graphql', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query: operation.text,
      variables,
    }),
  }).then(response => {
    return response.json();
  });
}

const environment = new Environment({
  network: Network.create(fetchQuery),
  store: new Store(new RecordSource()),  
});

export default class App extends React.Component {
  render() {
    return (
      <QueryRenderer
        environment={environment}
        query={graphql`
          query AppQuery {
            rebels {
              name
            }  
          }
        `}
        variables={{}}
        render={({error, props}) => {
          if (error) {
            return <div>Error! ha!</div>;
          }
          if (!props) {
            return <div>Loading...</div>;
          }
          return <div>Newton ID: {props.rebels.name}</div>;
        }}
      />
    );
  }
}
