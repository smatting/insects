/**
 * @flow
 */

/* eslint-disable */

'use strict';

/*::
import type { ReaderFragment } from 'relay-runtime';
import type { FragmentReference } from "relay-runtime";
declare export opaque type ShipComponent_ship$ref: FragmentReference;
declare export opaque type ShipComponent_ship$fragmentType: ShipComponent_ship$ref;
export type ShipComponent_ship = {|
  +id: string,
  +name: ?string,
  +$refType: ShipComponent_ship$ref,
|};
export type ShipComponent_ship$data = ShipComponent_ship;
export type ShipComponent_ship$key = {
  +$data?: ShipComponent_ship$data,
  +$fragmentRefs: ShipComponent_ship$ref,
};
*/


const node/*: ReaderFragment*/ = {
  "kind": "Fragment",
  "name": "ShipComponent_ship",
  "type": "Ship",
  "metadata": null,
  "argumentDefinitions": [],
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
      "name": "name",
      "args": null,
      "storageKey": null
    }
  ]
};
// prettier-ignore
(node/*: any*/).hash = 'ea42ed073d639077e53608c8124d0dea';
module.exports = node;
