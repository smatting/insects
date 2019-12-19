/**
 * @flow
 */

/* eslint-disable */

'use strict';

/*::
import type { ReaderFragment } from 'relay-runtime';
import type { FragmentReference } from "relay-runtime";
declare export opaque type FramePreview_frame$ref: FragmentReference;
declare export opaque type FramePreview_frame$fragmentType: FramePreview_frame$ref;
export type FramePreview_frame = {|
  +url: string,
  +$refType: FramePreview_frame$ref,
|};
export type FramePreview_frame$data = FramePreview_frame;
export type FramePreview_frame$key = {
  +$data?: FramePreview_frame$data,
  +$fragmentRefs: FramePreview_frame$ref,
};
*/


const node/*: ReaderFragment*/ = {
  "kind": "Fragment",
  "name": "FramePreview_frame",
  "type": "Frame",
  "metadata": null,
  "argumentDefinitions": [],
  "selections": [
    {
      "kind": "ScalarField",
      "alias": null,
      "name": "url",
      "args": null,
      "storageKey": null
    }
  ]
};
// prettier-ignore
(node/*: any*/).hash = 'ecb1c036e262dbced741572a9af09a3a';
module.exports = node;
