import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.framerate = 5
    try:
        for i, filename in enumerate(camera.capture_continuous('data/image{counter:02d}.jpg')):
            print(filename)
            if i == 20:
                break
    finally:
        camera.stop_preview()
