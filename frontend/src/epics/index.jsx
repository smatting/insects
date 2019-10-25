import { ajax } from 'rxjs/ajax';
import { combineEpics, ofType } from 'redux-observable';
import { of } from 'rxjs';
import { map, catchError, concatMap, tap, withLatestFrom, filter, debounceTime, delay, mapTo } from 'rxjs/operators';
import * as a from '../actions';
import { BACKEND_URL } from '../config'


const makeURL = (action, state) => {
    const {lat, lon} = state.location;
    const query = action.query;
    return (BACKEND_URL + '/search?query=' + query + '&lat=' + lat + '&lon=' + lon)
}


const epics = combineEpics(

);

export default epics;
