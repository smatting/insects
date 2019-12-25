#!/usr/env python

####
# Downloads all insect frames listed in postgres captured by the RPi Cam through the gAPI.
####

import os

import wget
import psycopg2
import pandas as pd

FORCE_OVERWRITE = False

POSTGRES_URI = os.environ.get('POSTGRES_URI')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGES_DB = os.environ.get('POSTGES_DB')


def main2():
    "Downloads samples from each date."
    with psycopg2.connect(host=POSTGRES_URI, user=POSTGRES_USER,
                          password=POSTGRES_PASSWORD, dbname=POSTGES_DB) as conn:
        df = pd.read_sql("select id_new, date_trunc('day', time_stamp) as date from public.src_frame_newname", conn)
        for date, grp in df.groupby('date'):

            print(date)

            id_new = grp.iloc[0, :].id_new
            id_new_flat = id_new.replace('/', '_')
            download(f'https://storage.googleapis.com/eco1/frames/{id_new}',
                        f'/tmp/insects/{id_new_flat}')

            id_new = grp.iloc[int(len(grp)/2), :].id_new
            id_new_flat = id_new.replace('/', '_')
            download(f'https://storage.googleapis.com/eco1/frames/{id_new}',
                        f'/tmp/insects/{id_new_flat}')

            id_new = grp.iloc[-1, :].id_new
            id_new_flat = id_new.replace('/', '_')
            download(f'https://storage.googleapis.com/eco1/frames/{id_new}',
                        f'/tmp/insects/{id_new_flat}')


def main():
    "Downloads frames in general."
    with psycopg2.connect(host=POSTGRES_URI, user=POSTGRES_USER,
                          password=POSTGRES_PASSWORD, dbname=POSTGES_DB) as conn:

        df = pd.read_sql("select id_new from public.src_frame_newname where time_stamp >= '2019-11-16' and time_stamp < '2019-12-24'", conn)
        df = df.sample(1000, random_state=1)

        print(f'found {len(df)} entries, downloading...')
        for id_new in df['id_new']:
            id_new_flat = id_new.replace('/', '_')
            download(f'https://storage.googleapis.com/eco1/frames/{id_new}',
                        f'd00original/{id_new_flat}')


def download(_from, _to):
    if not os.path.exists(_to) or FORCE_OVERWRITE:
        print(f'{_from} => {_to}')
        wget.download(_from, _to)
        print('\n')
    else:
        print(f'{_to} exists, skipping.')


if __name__ == '__main__':
    main()
