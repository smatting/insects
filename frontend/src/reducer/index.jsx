import { combineReducers } from "redux";
import { createReducer } from "redux-starter-kit";
import { productsInit, basketInit } from "./dummy";
import _ from "lodash";

const dummyClips = [
  {
    id: "1",
    images: ["1", "2", "4", "5"],
    session: "Bug",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "2",
    images: ["1", "2", "4", "5"],
    session: "Bug",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "3",
    images: ["1", "2", "4", "5"],
    session: "Bug",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "4",
    images: ["1", "2", "4", "5"],
    session: "Butterfly",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "5",
    images: ["1", "2", "4", "5"],
    session: "Butterfly",
    thumbURL: "https://picsum.photos/200/300"
  }
];
const dummyImages = [
  {
    id: "1",
    url: "https://picsum.photos/200/300",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "2",
    img: "https://picsum.photos/200/300",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "3",
    img: "https://picsum.photos/200/300",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "4",
    img: "https://picsum.photos/200/300",
    thumbURL: "https://picsum.photos/200/300"
  },
  {
    id: "5",
    img: "https://picsum.photos/200/300",
    thumbURL: "https://picsum.photos/200/300"
  }
];
const dummyAnnotation = [
  { id: "1", images: ["1", "2"], labels: ["butterfly"] }
];
const dummySelection = { clipId: "1", firstImgId: "2", lastImgId: "4" };

const view = createReducer("OVERVIEW", {
  VIEW_UPDATE: (state, action) => action.view
});

const liveImage = createReducer(null, {
  LIVEIMAGE_NEW: (state, action) => action.liveImage
});

const key = list => ({
  byKey: _.keyBy(list, "id"),
  allIds: _.map(list, ({ id }) => id)
});

const annotation = createReducer(key(dummyAnnotation), {});

const images = createReducer(key(dummyImages), {});

const groupIds = (list, groupKey) =>
  _.mapValues(_.groupBy(list, groupKey), l => _.map(l, ({ id }) => id));

const keyClips = list => ({
  ...key(list),
  groupIds: groupIds(list, "session")
});

const clips = createReducer(keyClips(dummyClips), {});

const selection = createReducer(dummySelection, {});

const reducers = combineReducers({
  view,
  annotation,
  images,
  clips,
  selection,
  liveImage
});

export default reducers;
