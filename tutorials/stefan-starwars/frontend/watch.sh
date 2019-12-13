#!/usr/bin/env bash

flow-watch () {
  flow status;
  fswatch -e "/\." -o . | xargs -n1 -I{} flow status;
}

flow-watch
