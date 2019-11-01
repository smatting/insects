# Insect detector
The goal of this sub-project is to write an insect dector that takes an image as input and returns a bounding box for every insect in the image.

## Colab notebook
A colab notebook contains the code to train and evaluate the model. It can be found in the shared gdrive folder `insects/insectdetector`. One version contains additional explanations, the other is for faster working with less explanatory clutter.

## Data location
Since the data cannot be stored in GitLab, it can be found on gdrive under https://drive.google.com/drive/folders/1y2kLKmVjlW9kHQI78P0vhC4fZ7fVLFPr?usp=sharing. The notebooks can connect to this folder.

## Data
We require large amount of positive samples. That means images with insects and an associated bounding box. We can try to find as many as possible for free, but might have to resort to some bounding box tagging nevertheless.

See under [dataprepration/](datapreparation/) for more details.

The final version of the different prepared datasets can be found under [dataprepared/](dataprepared/).

## Idea
Using the YoLo net might work. Use Oskar's tushiseeder notes as base.
