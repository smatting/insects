# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
res = (2592, 1944)
camera.resolution = res
camera.framerate = 1
rawCapture = PiRGBArray(camera, size=res)

# allow the camera to warmup
time.sleep(0.5)

# capture frames from the camera
for i, frame in enumerate(camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

    cv2.imwrite("test{i}.jpg", image)

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
