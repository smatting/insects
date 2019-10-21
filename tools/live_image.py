import subprocess
import numpy as np
import cv2
import time

TEMP_FOLDER = '../temp'
REMOTE_ADDRESS = "pi@192.168.178.70"
REMOTE_FOLDER  = "/media/usb/cam1/frames"
REFRESH_MS = 200


def get_latest_file():
    command = f"ssh {REMOTE_ADDRESS} ls -l --full-time {REMOTE_FOLDER}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    last_line = str(output).split("\\n")[-2]
    filename = last_line.split(" ")[-1]
    return filename


def copy_file(filename):
    origin_path = f"{REMOTE_FOLDER}/{filename}"
    dest_path = f"{TEMP_FOLDER}/{filename}"
    command = f"scp {REMOTE_ADDRESS}:{origin_path} {dest_path}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return dest_path


def show_image(path):
    # Load an color image in grayscale
    img = cv2.imread(path)
    cv2.imshow('image', img)
    cv2.waitKey(REFRESH_MS)


def main():
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    last_filename = None
    while True:
        filename = get_latest_file()
        if filename != last_filename:
            path = copy_file(filename)
            last_filename = filename
        show_image(path)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
