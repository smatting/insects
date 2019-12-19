/**
 * @flow
 * @relayHash 79057e0ad33f8b769e9766ddb4bf4ac0
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
type FramePreview_frame$ref = any;
export type ClipQueryVariables = {||};
export type ClipQueryResponse = {|
  +clip: ?{|
    +frames: {|
      +edges: $ReadOnlyArray<?{|
        +node: ?{|
          +id: string,
          +$fragmentRefs: FramePreview_frame$ref,
        |}
      |}>
    |}
  |}
|};
export type ClipQuery = {|
  variables: ClipQueryVariables,
  response: ClipQueryResponse,
|};
*/


/*
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
    id
  }
}

fragment FramePreview_frame on Frame {
  url
}
*/

const node/*: ConcreteRequest*/ = (function(){
var v0 = [
  {
    "kind": "Literal",
    "name": "id",
    "value": "Q2xpcDoyODQ4"
  }
],
v1 = {
  "kind": "ScalarField",
  "alias": null,
  "name": "id",
  "args": null,
  "storageKey": null
};
return {
  "kind": "Request",
  "fragment": {
    "kind": "Fragment",
    "name": "ClipQuery",
    "type": "Query",
    "metadata": null,
    "argumentDefinitions": [],
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "name": "clip",
        "storageKey": "clip(id:\"Q2xpcDoyODQ4\")",
        "args": (v0/*: any*/),
        "concreteType": "Clip",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "name": "frames",
            "storageKey": null,
            "args": null,
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
                      (v1/*: any*/),
                      {
                        "kind": "FragmentSpread",
                        "name": "FramePreview_frame",
                        "args": null
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  "operation": {
    "kind": "Operation",
    "name": "ClipQuery",
    "argumentDefinitions": [],
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "name": "clip",
        "storageKey": "clip(id:\"Q2xpcDoyODQ4\")",
        "args": (v0/*: any*/),
        "concreteType": "Clip",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "name": "frames",
            "storageKey": null,
            "args": null,
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
                      (v1/*: any*/),
                      {
                        "kind": "ScalarField",
                        "alias": null,
                        "name": "url",
                        "args": null,
                        "storageKey": null
                      }
                    ]
                  }
                ]
              }
            ]
          },
          (v1/*: any*/)
        ]
      }
    ]
  },
  "params": {
    "operationKind": "query",
    "name": "ClipQuery",
    "id": null,
    "text": "query ClipQuery {\n  clip(id: \"Q2xpcDoyODQ4\") {\n    frames {\n      edges {\n        node {\n          id\n          ...FramePreview_frame\n        }\n      }\n    }\n    id\n  }\n}\n\nfragment FramePreview_frame on Frame {\n  url\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = 'de5ee2f5cb7c19ccaa91cc60be015acb';
module.exports = node;
