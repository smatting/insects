#!/usr/bin/env python3

"""
Create the required test-train splitfiles for training.
"""

import os
import sys
import random
import argparse

import numpy as np


#BASEPATH = '/content/gdrive/My Drive/darknet/data/insects/'
BASEPATH = '/content/darknet/data/'


def main():
    parser = argparse.ArgumentParser(description='Create a train/test.txt split. Each dataset is shuffled and split on its own (stratified random sampling).')
    parser.add_argument('trgdir', help='Where to create the split files.')
    parser.add_argument('datasets', nargs='+', help='Path to the datasets main directories.')
    parser.add_argument('--seed', type=int, default=1, help='Random seed for reproducible results.')
    parser.add_argument('--ratio', type=float, default=0.8, help='Train : test split ratio.')
    args = parser.parse_args()

    assert args.ratio <= 1.0 and args.ratio > 0.0

    random.seed(args.seed)

    datasetfiles = {}
    for datasetdir in args.datasets:

        datasetdir = datasetdir.strip().rstrip("/")

        # assume last path dir to be the dataset name
        datasetname = datasetdir.split('/')[-1]

        # try to find the sub directory containing the prepared images
        imagedatadir = None
        for subdir in next(os.walk(datasetdir))[1]:
            if 'prepareddata' in subdir:
                imagedatadir = subdir
        if imagedatadir is None:
            raise Exception(f'No sub-directory named like prepareddata found in {datasetdir} of {datasetname}.')

        datasetfiles[datasetname] = next(os.walk(os.path.join(datasetdir, imagedatadir, 'images')))[2]
        datasetfiles[datasetname] = [fname for fname in datasetfiles[datasetname] if not fname.endswith('.txt')]

    print(f'Parsed datasets {datasetfiles.keys()}.')

    # soplit into train and test sets using stratified random sampling
    train_files = []
    test_files = []
    for k in sorted(datasetfiles.keys()):  # lexical order ensures smae results independent of script argument order passing

        random.shuffle(datasetfiles[k])
        files = [os.path.join(BASEPATH, k, 'images', f) for f in datasetfiles[k]]

        sidx = int(args.ratio * len(files))
        train_files.extend(sorted(files[:sidx]))
        test_files.extend(sorted(files[sidx:]))

    print('Split into {} train and {} test files.'.format(len(train_files), len(test_files)))

    with open(os.path.join(args.trgdir, 'train.txt'), 'w') as f:
        for fn in train_files:
            f.write(fn + '\n')

    with open(os.path.join(args.trgdir, 'test.txt'), 'w') as f:
        for fn in test_files:
            f.write(fn + '\n')

    print(f'Sucessfully created test.txt and train.txt in {args.trgdir}.')

if __name__ == '__main__':
    main()
