#!/usr/bin/env python3

"""Extracts bounding boxes from XML format into a yolo bbox format."""

import glob
import xml.etree.ElementTree as ET


def parse_element_int(root, name):
    "Returns int vale of first occurence of element in root."
    for _x in root.iter(name):
        return int(_x.text)


print('START')

for fn in glob.glob(f'00original/Annotations/*.xml'):

    try:
        root = ET.parse(fn).getroot()

        image_width = parse_element_int(root, 'width')
        image_height = parse_element_int(root, 'height')
        x0 = parse_element_int(root, 'xmin')
        x1 = parse_element_int(root, 'xmax')
        y0 = parse_element_int(root, 'ymin')
        y1 = parse_element_int(root, 'ymax')

        objectid = 0
        x = (x0 + (x1 - x0) / 2) / image_width  # normalized center of box
        y = (y0 + (y1 - y0) / 2) / image_height  # normalized center of box
        width = (x1 - x0) / image_width  # normalized width of box
        height = (y1 - y0) / image_height  # normalized height of box

        #print('x0', x0, 'x1', x1, 'y0', y0, 'y1', y1)
        #print('imagewidth', image_width, 'image_height', image_height)

        fn_new = fn.split('/')[-1][:-4]
        fn_new = f'01boundingboxes/{fn_new}.txt'

        with open(fn_new, 'w') as f:
            f.write(f'{objectid} {x} {y} {width} {height}')  # yolo bbox format

        print('.', end='')
    except Exception as e:
        print(f'failed parsing on {fn}!')

print('DONE')
