import {
  Environment,
  Network,
  RecordSource,
  Store,
} from 'relay-runtime';

const fetchQuery = (operation,variables) => {
    return fetch('http://0.0.0.0:8000/graphql', {
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

export default new Environment({
  network: Network.create(fetchQuery),
  store: new Store(new RecordSource()),
});
