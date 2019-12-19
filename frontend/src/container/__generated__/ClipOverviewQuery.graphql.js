/**
 * @flow
 * @relayHash 9ad8d4af9fd539737912f248386ade67
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
type ClipPreview_previewFrame$ref = any;
export type ClipOverviewQueryVariables = {||};
export type ClipOverviewQueryResponse = {|
  +allClips: ?{|
    +edges: $ReadOnlyArray<?{|
      +node: ?{|
        +id: string,
        +previewFrame: ?{|
          +$fragmentRefs: ClipPreview_previewFrame$ref
        |},
      |}
    |}>
  |}
|};
export type ClipOverviewQuery = {|
  variables: ClipOverviewQueryVariables,
  response: ClipOverviewQueryResponse,
|};
*/


/*
query ClipOverviewQuery {
  allClips(first: 20) {
    edges {
      node {
        id
        previewFrame {
          ...ClipPreview_previewFrame
          id
        }
      }
    }
  }
}

fragment ClipPreview_previewFrame on Frame {
  url
}
*/

const node/*: ConcreteRequest*/ = (function(){
var v0 = [
  {
    "kind": "Literal",
    "name": "first",
    "value": 20
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
    "name": "ClipOverviewQuery",
    "type": "Query",
    "metadata": null,
    "argumentDefinitions": [],
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "name": "allClips",
        "storageKey": "allClips(first:20)",
        "args": (v0/*: any*/),
        "concreteType": "ClipConnection",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "name": "edges",
            "storageKey": null,
            "args": null,
            "concreteType": "ClipEdge",
            "plural": true,
            "selections": [
              {
                "kind": "LinkedField",
                "alias": null,
                "name": "node",
                "storageKey": null,
                "args": null,
                "concreteType": "Clip",
                "plural": false,
                "selections": [
                  (v1/*: any*/),
                  {
                    "kind": "LinkedField",
                    "alias": null,
                    "name": "previewFrame",
                    "storageKey": null,
                    "args": null,
                    "concreteType": "Frame",
                    "plural": false,
                    "selections": [
                      {
                        "kind": "FragmentSpread",
                        "name": "ClipPreview_previewFrame",
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
    "name": "ClipOverviewQuery",
    "argumentDefinitions": [],
    "selections": [
      {
        "kind": "LinkedField",
        "alias": null,
        "name": "allClips",
        "storageKey": "allClips(first:20)",
        "args": (v0/*: any*/),
        "concreteType": "ClipConnection",
        "plural": false,
        "selections": [
          {
            "kind": "LinkedField",
            "alias": null,
            "name": "edges",
            "storageKey": null,
            "args": null,
            "concreteType": "ClipEdge",
            "plural": true,
            "selections": [
              {
                "kind": "LinkedField",
                "alias": null,
                "name": "node",
                "storageKey": null,
                "args": null,
                "concreteType": "Clip",
                "plural": false,
                "selections": [
                  (v1/*: any*/),
                  {
                    "kind": "LinkedField",
                    "alias": null,
                    "name": "previewFrame",
                    "storageKey": null,
                    "args": null,
                    "concreteType": "Frame",
                    "plural": false,
                    "selections": [
                      {
                        "kind": "ScalarField",
                        "alias": null,
                        "name": "url",
                        "args": null,
                        "storageKey": null
                      },
                      (v1/*: any*/)
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
  "params": {
    "operationKind": "query",
    "name": "ClipOverviewQuery",
    "id": null,
    "text": "query ClipOverviewQuery {\n  allClips(first: 20) {\n    edges {\n      node {\n        id\n        previewFrame {\n          ...ClipPreview_previewFrame\n          id\n        }\n      }\n    }\n  }\n}\n\nfragment ClipPreview_previewFrame on Frame {\n  url\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = '75c1ee909108522d1da12eb6e6debf3d';
module.exports = node;
