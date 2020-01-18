/**
 * @flow
 * @relayHash 05910fedb2e40e43f206c2a6e5cc335f
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
export type FramesQueryVariables = {||};
export type FramesQueryResponse = {|
  +frames: ?$ReadOnlyArray<?{|
    +id: string,
    +url: string,
    +timestamp: any,
    +thumbnail: string,
  |}>
|};
export type FramesQuery = {|
  variables: FramesQueryVariables,
  response: FramesQueryResponse,
|};
*/


/*
query FramesQuery {
  frames(tbegin: "2019-11-01T00:00:00", tend: "2019-11-15T00:00:00", nframes: 10) {
    id
    url
    timestamp
    thumbnail
  }
}
*/

const node/*: ConcreteRequest*/ = (function(){
var v0 = [
  {
    "kind": "LinkedField",
    "alias": null,
    "name": "frames",
    "storageKey": "frames(nframes:10,tbegin:\"2019-11-01T00:00:00\",tend:\"2019-11-15T00:00:00\")",
    "args": [
      {
        "kind": "Literal",
        "name": "nframes",
        "value": 10
      },
      {
        "kind": "Literal",
        "name": "tbegin",
        "value": "2019-11-01T00:00:00"
      },
      {
        "kind": "Literal",
        "name": "tend",
        "value": "2019-11-15T00:00:00"
      }
    ],
    "concreteType": "Frame",
    "plural": true,
    "selections": [
      {
        "kind": "ScalarField",
        "alias": null,
        "name": "id",
        "args": null,
        "storageKey": null
      },
      {
        "kind": "ScalarField",
        "alias": null,
        "name": "url",
        "args": null,
        "storageKey": null
      },
      {
        "kind": "ScalarField",
        "alias": null,
        "name": "timestamp",
        "args": null,
        "storageKey": null
      },
      {
        "kind": "ScalarField",
        "alias": null,
        "name": "thumbnail",
        "args": null,
        "storageKey": null
      }
    ]
  }
];
return {
  "kind": "Request",
  "fragment": {
    "kind": "Fragment",
    "name": "FramesQuery",
    "type": "Query",
    "metadata": null,
    "argumentDefinitions": [],
    "selections": (v0/*: any*/)
  },
  "operation": {
    "kind": "Operation",
    "name": "FramesQuery",
    "argumentDefinitions": [],
    "selections": (v0/*: any*/)
  },
  "params": {
    "operationKind": "query",
    "name": "FramesQuery",
    "id": null,
    "text": "query FramesQuery {\n  frames(tbegin: \"2019-11-01T00:00:00\", tend: \"2019-11-15T00:00:00\", nframes: 10) {\n    id\n    url\n    timestamp\n    thumbnail\n  }\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = '4651a29970575a3be30956bf157c2feb';
module.exports = node;
