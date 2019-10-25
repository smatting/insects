# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import datetime
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (2592, 1944)
# camera.resolution = '1080p'
camera.framerate = 1
# camera.exposure_mode='sports'
rawCapture = PiRGBArray(camera, size=camera.resolution)

# allow the camera to warmup
time.sleep(1)

# capture frames from the camera
for i, frame in enumerate(camera.capture_continuous(rawCapture, format="bgr", use_video_port=False)):
    image = frame.array

    date_str = datetime.datetime.now().isoformat()

    cv2.imwrite("data/test_{s}.png".format(s=date_str), image)
    rawCapture.truncate(0)
    if i > 20:
        break
