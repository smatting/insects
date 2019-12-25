#!/usr/bin/env python3

"""
Parses a VGG VIA (http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html) generated annotation file
into the format required by the darknet trainer.
usage: <scipt> <annotation_file.csv> <images-dir> <target_dir>
"""

import os
import sys
import json

from PIL import Image
import pandas as pd
from pandas.io.json import json_normalize


OBJECT_CLASS = 0


def main():
    fn = sys.argv[1]
    idir = sys.argv[2]
    odir = sys.argv[3]

    # check output dir empty
    if os.listdir(odir):
        print(f"Error: Traget dir {odir} must be empty.")
        return

    # read and keep only required columns
    df = pd.read_csv(fn, sep=',')
    df = df[['filename', 'region_shape_attributes']]

    # parse json string into proper columns and index with filename
    df_rsa = json_normalize(df['region_shape_attributes'].apply(json.loads))
    df_rsa = df_rsa.merge(df['filename'], left_index=True, right_index=True)
    df_rsa = df_rsa.set_index(df['filename'])

    # drop nans (NaN means invalid or not set rectangle)
    df_rsa = df_rsa.dropna()

    # append to annotation files
    for index, row in df_rsa.iterrows():
        basefn = os.path.splitext(index)[0] + '.txt'
        trgfn = os.path.join(odir, basefn)
        print(trgfn)

        if not os.path.exists(os.path.join(idir, index)):
            print("No image named {fpath}. Skipping.".format(os.path.join(idir, index)))
            continue

        im = Image.open(os.path.join(idir, index))
        width, height = im.size

        with open(trgfn, 'a') as f:
            f.write('{} {} {} {} {}\n'.format(
                OBJECT_CLASS,
                (row['x'] + row['width'] / 2.) / width,
                (row['y'] + row['height'] / 2.) / height,
                row['width'] / width,
                row['height'] / height
            ))


if __name__ == '__main__':
    main()
