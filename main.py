# This file we will import all of our other functions / call our function
import os
# Vision: python yolov5/detect.py --source 0 --classes 0
import Speaking as sp
from getText import getText
def initializeCam():
    sp.speak("Hello, I'm B. Washington. How may I help you?")
    while True:

        #print("initializing camera")

        os.system("python yolov5/detect.py --source 0 --classes 0")

        #print("What color is the sky?")
        # decision = input("enter a color ")
        sp.Speaking()

        #if decision == "done":
            #break

initializeCam()

