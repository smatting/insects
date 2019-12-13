/**
 * @flow
 */

/* eslint-disable */

'use strict';

/*::
import type { ReaderFragment } from 'relay-runtime';
import type { FragmentReference } from "relay-runtime";
declare export opaque type ClipPreview_previewFrame$ref: FragmentReference;
declare export opaque type ClipPreview_previewFrame$fragmentType: ClipPreview_previewFrame$ref;
export type ClipPreview_previewFrame = {|
  +url: string,
  +$refType: ClipPreview_previewFrame$ref,
|};
export type ClipPreview_previewFrame$data = ClipPreview_previewFrame;
export type ClipPreview_previewFrame$key = {
  +$data?: ClipPreview_previewFrame$data,
  +$fragmentRefs: ClipPreview_previewFrame$ref,
};
*/


const node/*: ReaderFragment*/ = {
  "kind": "Fragment",
  "name": "ClipPreview_previewFrame",
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
(node/*: any*/).hash = '01c2333443fd5189378a424e4800b715';
module.exports = node;
