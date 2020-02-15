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

const collection = createReducer(
  { frames: key([]), currentFrameId: null },
  {
    COLLECTION_LOADED: (state, action) => ({
      id: action.collection.id,
      frames: key(action.collection.frames),
      currentFrameId: action.collection.frames[0].id
    })
  }
);

const appearances = createReducer(key([]), {
  APPEARANCE_ADDED: (state, action) => ({
    byKey: { ...state.byKey, [action.appearance.id]: action.appearance },
    allIds: [...state.allIds, action.appearance.id]
  })
});

const species = createReducer(key([]), {
  SERVER_INIT: (state, action) => key(action.species)
});

const defaultSearch = {
  startDate: new Date("2019-11-15T00:00:00"),
  endDate: new Date("2020-01-31T00:00:00")
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
  liveImage,
  appearances,
  collection,
  species
});

export default reducers;
