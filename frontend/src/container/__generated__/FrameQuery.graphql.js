/**
 * @flow
 * @relayHash 98acb6113193ba3f01413b06755166fd
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
export type FrameQueryVariables = {||};
export type FrameQueryResponse = {|
  +frame: ?{|
    +id: string,
    +url: string,
  |}
|};
export type FrameQuery = {|
  variables: FrameQueryVariables,
  response: FrameQueryResponse,
|};
*/


/*
query FrameQuery {
  frame(id: "RnJhbWU6MjM1NjU5") {
    id
    url
  }
}
*/

const node/*: ConcreteRequest*/ = (function(){
var v0 = [
  {
    "kind": "LinkedField",
    "alias": null,
    "name": "frame",
    "storageKey": "frame(id:\"RnJhbWU6MjM1NjU5\")",
    "args": [
      {
        "kind": "Literal",
        "name": "id",
        "value": "RnJhbWU6MjM1NjU5"
      }
    ],
    "concreteType": "Frame",
    "plural": false,
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
      }
    ]
  }
];
return {
  "kind": "Request",
  "fragment": {
    "kind": "Fragment",
    "name": "FrameQuery",
    "type": "Query",
    "metadata": null,
    "argumentDefinitions": [],
    "selections": (v0/*: any*/)
  },
  "operation": {
    "kind": "Operation",
    "name": "FrameQuery",
    "argumentDefinitions": [],
    "selections": (v0/*: any*/)
  },
  "params": {
    "operationKind": "query",
    "name": "FrameQuery",
    "id": null,
    "text": "query FrameQuery {\n  frame(id: \"RnJhbWU6MjM1NjU5\") {\n    id\n    url\n  }\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = '6c2050621a2d4a948f98f4fca6a62dec';
module.exports = node;
