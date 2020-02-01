import { combineReducers } from "redux";
import { createReducer } from "redux-starter-kit";
import _ from "lodash";

const view = createReducer("FRAME", {
  VIEW_UPDATE: (state, action) => action.view
});

const liveImage = createReducer(null, {
  LIVEIMAGE_NEW: (state, action) => action.liveImage
});

const key = list => ({
  byKey: _.keyBy(list, "id"),
  allIds: _.map(list, ({ id }) => id)
});

const defaultSearch = {
  startDate: new Date("2019-10-01T00:00:00"),
  endDate: new Date("2019-12-31T00:00:00")
};

const search = createReducer(defaultSearch, {
  SEARCH_UPDATE: (state, action) => ({ ...state, ...action.search })
});

const searchResults = createReducer(
  { frames: [], ntotal: 0 },
  {
    SEARCH_UPDATED: (state, action) => action.searchResults
  }
);

const reducers = combineReducers({
  view,
  search,
  searchResults,
  liveImage
});

export default reducers;
