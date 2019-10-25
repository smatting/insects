import { combineReducers } from "redux";
import { createReducer } from "redux-starter-kit";
import { productsInit, basketInit } from "./dummy";

const view = createReducer("CLIP", {
  VIEW_UPDATE: (state, action) => action.view
});

const reducers = combineReducers({
  view
});

export default reducers;
