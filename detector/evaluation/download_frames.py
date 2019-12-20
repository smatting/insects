#!/usr/env python

####
# Downloads all insect frames listed in postgres captured by the RPi Cam through the gAPI.
####

import os

import wget
import psycopg2
import pandas as pd

DATA_TYPE = 'src' # 'src' | 'insects'
FORCE_OVERWRITE = False

POSTGRES_URI = os.environ.get('POSTGRES_URI')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGES_DB = os.environ.get('POSTGES_DB')


def main():
    with psycopg2.connect(host=POSTGRES_URI, user=POSTGRES_USER,
                          password=POSTGRES_PASSWORD, dbname=POSTGES_DB) as conn:

        if 'src' == DATA_TYPE:
            df = pd.read_sql('select id_new from public.src_frame_newname order by time_stamp ASC limit 10000', conn)

            print(f'found {len(df)} entries, downloading...')
            for id_new in df['id_new']:
                id_new_flat = id_new.replace('/', '_')
                download(f'https://storage.googleapis.com/eco1/frames/{id_new}',
                         f'data/src_frame/{id_new_flat}')

        elif 'insects' == DATA_TYPE:
            df = pd.read_sql('select url from public.insects_frame limit 100', conn)

            print(f'found {len(df)} entries, downloading...')
            for url in df['url']:
                id_new = url.split('frames/')[-1]
                id_new_flat = id_new.replace('/', '_')
                download(url, f'data/insects_frame/{id_new_flat}')

        else:
            print(f'error: unkown value for DATA_TYPE {DATA_TYPE}')


def download(_from, _to):
    if not os.path.exists(_to) or FORCE_OVERWRITE:
        print(f'{_from} => {_to}')
        wget.download(_from, _to)
        print('\n')
    else:
        print(f'{_to} exists, skipping.')


if __name__ == '__main__':
    main()
