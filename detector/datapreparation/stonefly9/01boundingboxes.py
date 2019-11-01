#!/usr/bin/env python3

"""Extracts bounding boxes from mask images into a yolo bbox format."""

import glob

import numpy as np
from PIL import Image
from scipy import ndimage

for _dir in glob.glob('00original/features/*'):

    for _set in ['set0', 'set1', 'set2']:

        for fn in glob.glob(f'{_dir}/segmentation/{_set}/*.new.sg.png'):

            print(f'processing {fn}')

            img = Image.open(fn)
            img = np.asarray(img).T  # note T, since seems to be loaded HxW rather than WxH

            objs = ndimage.find_objects(img.astype(np.uint8))
            x0 = objs[0][0].start
            x1 = objs[0][0].stop
            y0 = objs[0][1].start
            y1 = objs[0][1].stop

            objectid = 0
            x = (x0 + (x1 - x0) / 2) / img.shape[0]  # normalized center of box
            y = (y0 + (y1 - y0) / 2) / img.shape[1]  # normalized center of box
            width = (x1 - x0) / img.shape[0]  # normalized width of box
            height = (y1 - y0) / img.shape[1]  # normalized height of box

            fn_new = fn.split('/')[-1][:-11]
            fn_new = f'01boundingboxes/{fn_new}.txt'

            with open(fn_new, 'w') as f:
                f.write(f'{objectid} {x} {y} {width} {height}')  # yolo bbox format

            print(f'\tsaved as {fn_new}')

print('DONE')
