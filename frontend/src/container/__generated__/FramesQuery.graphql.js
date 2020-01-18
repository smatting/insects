/**
 * @flow
 * @relayHash ac32104961f9eafd0cfd23e2a476f04d
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
export type FramesQueryVariables = {|
  tbegin: any,
  tend: any,
|};
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
query FramesQuery(
  $tbegin: DateTime!
  $tend: DateTime!
) {
  frames(tbegin: $tbegin, tend: $tend, nframes: 10) {
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
    "kind": "LocalArgument",
    "name": "tbegin",
    "type": "DateTime!",
    "defaultValue": null
  },
  {
    "kind": "LocalArgument",
    "name": "tend",
    "type": "DateTime!",
    "defaultValue": null
  }
],
v1 = [
  {
    "kind": "LinkedField",
    "alias": null,
    "name": "frames",
    "storageKey": null,
    "args": [
      {
        "kind": "Literal",
        "name": "nframes",
        "value": 10
      },
      {
        "kind": "Variable",
        "name": "tbegin",
        "variableName": "tbegin"
      },
      {
        "kind": "Variable",
        "name": "tend",
        "variableName": "tend"
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
    "argumentDefinitions": (v0/*: any*/),
    "selections": (v1/*: any*/)
  },
  "operation": {
    "kind": "Operation",
    "name": "FramesQuery",
    "argumentDefinitions": (v0/*: any*/),
    "selections": (v1/*: any*/)
  },
  "params": {
    "operationKind": "query",
    "name": "FramesQuery",
    "id": null,
    "text": "query FramesQuery(\n  $tbegin: DateTime!\n  $tend: DateTime!\n) {\n  frames(tbegin: $tbegin, tend: $tend, nframes: 10) {\n    id\n    url\n    timestamp\n    thumbnail\n  }\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = '965dca16cbc5e9339825432fedb41267';
module.exports = node;
