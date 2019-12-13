#!/bin/bash

./manage.py graphql_schema --out frontend/schema.json --watch &
./manage.py runserver &

cd frontend

npm relay --watch &
npm start
