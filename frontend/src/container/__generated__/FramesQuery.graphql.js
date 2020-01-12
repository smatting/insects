/**
 * @flow
 * @relayHash 7cb49aa6c9db6c67c37e2824c6043500
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
export type FramesQueryVariables = {||};
export type FramesQueryResponse = {|
  +allFrames: ?{|
    +edges: $ReadOnlyArray<?{|
      +node: ?{|
        +id: string,
        +url: string,
        +thumbUrl: ?string,
      |}
    |}>
  |}
|};
export type FramesQuery = {|
  variables: FramesQueryVariables,
  response: FramesQueryResponse,
|};
*/


/*
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
*/

const node/*: ConcreteRequest*/ = (function(){
var v0 = [
  {
    "kind": "LinkedField",
    "alias": null,
    "name": "allFrames",
    "storageKey": "allFrames(url:\"test1\")",
    "args": [
      {
        "kind": "Literal",
        "name": "url",
        "value": "test1"
      }
    ],
    "concreteType": "FrameConnection",
    "plural": false,
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "name": "edges",
        "storageKey": null,
        "args": null,
        "concreteType": "FrameEdge",
        "plural": true,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "name": "node",
            "storageKey": null,
            "args": null,
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
              },
              {
                "kind": "ScalarField",
                "alias": null,
                "name": "thumbUrl",
                "args": null,
                "storageKey": null
              }
            ]
          }
        ]
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
    "text": "query FramesQuery {\n  allFrames(url: \"test1\") {\n    edges {\n      node {\n        id\n        url\n        thumbUrl\n      }\n    }\n  }\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = 'd11830eeeb383a6ba2ac42f226282c35';
module.exports = node;
