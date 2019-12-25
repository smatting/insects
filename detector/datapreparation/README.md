# Insect data
Pictures of insects with bounding boxes.

Ideally, the images are as near to the ones we will eventuall record with our camera.

For an overview of possible insect image databases available online see: https://docs.google.com/document/d/1cGW4GRWTNBiCHsz0ciN3PXXk2pueVC3QAmTzEFLWiXM/edit?usp=sharing

## Data format
YOLO expects an image with an associated label file in the same folder. Not all images have to reside in the same folder. The main configuration file for a training / testing is the `obj.data`. The lass names are detailed in `obj.names`. And the training and validation datasets in `train.txt` resp. `test.txt`.

Use `train_test_split.py` to generate the train and test splits.

## Databases

### [cricketsN/](crickets/)
- ID: cricketsN
- Source: Our own recordings
- N: N

Contains exactly N randomly picked images with crickets recorded by us. See the [README.md](crickets/) in the folder for more information.

### [coift/](coift/)
- ID: coift
- Source: http://www.vision.ime.usp.br/~lucyacm/thesis/coift.html
- N: 129

Contains a few hundred images with associated exact segmentation masks. All insects were recorded in good light and with the full body in various poses in natural surroundings.

Well usable. I can extract bounding boxes from the segmentation images.

### [stonefly9/](stonefly9/)
- ID: stonefly9
- Source: http://web.engr.oregonstate.edu/~tgd/bugid/stonefly9/
- N: 3844

Contains a few hundred images with associated rough segmentation masks. Contains only stoneflies, which are very small insects, recorded in petri-dishes with ok lightning conditions in various poses.

Can be used if enough other insect images are in the same training data. I can extract bounding boxes from the segmentation images.

### [IP102/](IP102/)
- ID: IP102
- Source: https://github.com/xpwu95/IP102
- N: 18975

Contains a few thousand insect images crawled from the web, usually in their natural surroundings and rather centered. Also contains associated bounding boxes for ~19k images.

Well usable. I can transform the bounding box format.

### [valan/](valan/)
- ID: valan
- Source: https://datadryad.org/stash/dataset/doi:10.5061/dryad.20ch6p5

Contains a few hundred images (or somethimes rather links to images) of very small insects of the same family. No segmentation. This dataset is rather for exacts type classification than insect detection purposes.

Not usable. Just one family and way to good and high resolution images. Furthermore, no segmentations or bounding boxes.