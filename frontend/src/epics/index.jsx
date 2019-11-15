import { ajax } from "rxjs/ajax";
import { combineEpics, ofType } from "redux-observable";
import { of } from "rxjs";
import {
  map,
  catchError,
  concatMap,
  tap,
  withLatestFrom,
  filter,
  debounceTime,
  delay,
  mapTo
} from "rxjs/operators";
import * as a from "../actions";

const epics = combineEpics();

export default epics;
