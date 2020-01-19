/**
 * @flow
 * @relayHash 128b6a85cd9d5bca95f895afeae4e6f4
 */

/* eslint-disable */

'use strict';

/*::
import type { ConcreteRequest } from 'relay-runtime';
export type BrowserQueryVariables = {|
  tbegin: any,
  tend: any,
|};
export type BrowserQueryResponse = {|
  +frames: ?$ReadOnlyArray<?{|
    +id: string,
    +url: string,
    +timestamp: any,
    +thumbnail: string,
  |}>
|};
export type BrowserQuery = {|
  variables: BrowserQueryVariables,
  response: BrowserQueryResponse,
|};
*/


/*
query BrowserQuery(
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
    "name": "BrowserQuery",
    "type": "Query",
    "metadata": null,
    "argumentDefinitions": (v0/*: any*/),
    "selections": (v1/*: any*/)
  },
  "operation": {
    "kind": "Operation",
    "name": "BrowserQuery",
    "argumentDefinitions": (v0/*: any*/),
    "selections": (v1/*: any*/)
  },
  "params": {
    "operationKind": "query",
    "name": "BrowserQuery",
    "id": null,
    "text": "query BrowserQuery(\n  $tbegin: DateTime!\n  $tend: DateTime!\n) {\n  frames(tbegin: $tbegin, tend: $tend, nframes: 10) {\n    id\n    url\n    timestamp\n    thumbnail\n  }\n}\n",
    "metadata": {}
  }
};
})();
// prettier-ignore
(node/*: any*/).hash = 'ab9d2bb2316b21f25f75d1802db99bad';
module.exports = node;
