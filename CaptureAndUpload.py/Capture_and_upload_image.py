from operator import truediv

from dropbox.dropbox_client import Dropbox
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()

        image_name = "img"+str(number)+".png"

        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    
    return image_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(image_name):
    access_Token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"

    file = image_name
    file_from = file
    file_to = "/testFolder/"+(image_name)
    dbx = dropbox.Dropbox(access_Token)

    with open(file_from, "rb") as f:
        dbx.file_upload(f.read(), file_to, mode = dropbox.file.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        if((time.time()-start_time)>= 5):
            name = take_snapshot()
            upload_file(name)

main()
        