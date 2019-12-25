# Crickets
Collective folder for all datasets created from our recorded crciket images. All images were recorded in November/December 2019 in a terrarium with the RPi camera under different lightning conditions. All considered images were marked by a motion event.

Different datasets of different sizes were created. Each larger one contains the images of all smaller ones. Annotations were created manually (see below for howto).


## Datasets

- Crickets100
- Crickets1000 (not yet annotated)
- Crickets10000 (not yet downloaded)


## Dataset preparation
A detailed description of how to get the data and how to annotate it.


### Collecting the data
The images recorded by the camera is accessible through gapis ([example](https://storage.googleapis.com/eco1/frames/cam1/2019-11-22/14/317-20191122140318-00.jpg)). The corresponding frame IDs can be read from the postgres DB (`postgresql://eco:{password}@195.201.97.57/eco`) with

```sql
select id_new from public.src_frame_newname order by time_stamp ASC limit 10
```

and entered in the access URI `https://storage.googleapis.com/eco1/frames/{id_new}`.

All returned frames were triggered by a movement event and are suspected to contain insects. Hence, they are the ideal candidates for an evaluation dataset. The download functionality is provided in the file [00download.py](00download.py).

After new recordings were generated, the data has to be collected again.

Note that many frames are actual no real insect recordings. Here we have to go by recording date:

- 2019-10-18: not insects from here
- 2019-11-16: from here insects

To achieve repetability, all frames were selected with the query `select id_new from public.src_frame_newname where time_stamp >= '2019-11-16' and time_stamp < '2019-12-24'`  and then a pandas `df.sample(N, random_state=1)` was performed before downloading the images.


### Annotating the data

With http://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html, the project is saved in the (02boundingboxes/)[02boundingboxes/] folder as JSON file. The labels are exported in CSV format into a file, which can then be parsed with `02annotationtransformer.py`. The final format is one text file per image (places in a different folder) with the same basename but `.txt` ending. The file should contain a single line for each object in the associated image with the format:

```bash
<object-id> <x> <y> <width> <height>
```

Note that the object-ids are continuous and zero-based class identifiers. The numeric values of the bounding-boxes are all not pixel integers, but rather fractions of the image width respectively height. And the x, y values denote not the top-left corner, but rather the center of the box. A file can contain between zero and any number of entries / lines.
