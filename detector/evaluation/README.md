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

