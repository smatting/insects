# Evaluation
The evaluation of the detector network is performed on images recorded in-sitio by the RPi camera of insects placed in the constructed terrarium. Unfortunately, we do not have any ground truth for these images. Hence the evaluation is purely qualitative and manual.

The evaluation is performed with the application (here used for evaluation) notebook: [https://colab.research.google.com/drive/1rXrkEkHEbQ30tvESCDI9nTefSsH5XVfW#scrollTo=iOsT0M-k9QE8](https://colab.research.google.com/drive/1rXrkEkHEbQ30tvESCDI9nTefSsH5XVfW#scrollTo=iOsT0M-k9QE8).

## Evaluation results

1. A network (tiny as well as full) trained on the full other insects training dataset failed to detect any of our Heimchens from any of the recording days. Unfortunately, it seems that the network has to be re-trained to detect the Heimchen.

## Evaluation dataset

### [eval_n100.tar.gx](https://drive.google.com/open?id=1JLRetkXjsA02xtABBdVqRTZzpS48A6KL)
Randomly selected 100 recorded frames with insects showing.


## Collecting the data
The images recorded by the camera is accessible through gapis ([example](https://storage.googleapis.com/eco1/frames/cam1/2019-11-22/14/317-20191122140318-00.jpg)). The corresponding frame IDs can be read from the postgres DB (`postgresql://eco:{password}@195.201.97.57/eco`) with

```sql
select id_new from public.src_frame_newname order by time_stamp ASC limit 10
```

and entered in the access URI `https://storage.googleapis.com/eco1/frames/{id_new}`.

All returned frames were triggered by a movement event and are suspected to contain insects. Hence, they are the ideal candidates for an evaluation dataset. The download functionality is provided in the file [download_frames.py](download_frames.py).

After new recordings were generated, the data has to be collected again.

Note that many frames are actual no real insect recordings. Here we have to go by recording date:

- 2019-10-18: not insects from here
- 2019-11-16: from here insects


### Annotation

With http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html, the project is saved locally as JSON file. The labels are exported in CSV format into a file, which can then be parsed with `scripts/annotation_transformer.py`. The final format is one text file per image (places in a different folder) with the same basename but `.txt` ending. The file should contain a single line for each object in the associated image with the format:

```bash
<object-id> <x> <y> <width> <height>
```

Note that the object-ids are continuous and zero-based class identifiers. The numeric values of the bounding-boxes are all not pixel integers, but rather fractions of the image width respectively height. And the x, y values denote not the top-left corner, but rather the center of the box. A file can contain between zero and any number of entries / lines.

Remember to put the folder “images” and folder “annotations” in the same parent directory, as the darknet code look for annotation files this way (by default).

Backups of the label creation data can be found in the `labelcreation/` subfolder.