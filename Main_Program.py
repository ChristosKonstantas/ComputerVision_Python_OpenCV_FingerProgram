import cv2
import time
import os
import mediapipe as mp
import PoseEstimation as posest
import HandTrackingModule as htm
import GestureMetric as gm
import eye_detect as eye
import FaceDetection as face
import counter
import SpeechRecognition as sr
import numpy as np
import math
import speech_recognition
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
wCam, hCam = 640, 480

cap=cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


pTime=0

detector=htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
tipIds = [4, 8, 12, 16, 20]

stop_count= 0
c_fig = 0




recognizer= speech_recognition.Recognizer()

while True:
     c_fig = counter.counterFunc(stop_count, tipIds, detector,cap)
     cv2.VideoCapture(0).release()
     cv2.destroyAllWindows()

     if c_fig == 0:
          print('no function')
     elif c_fig == 1:
          percentage = (gm.Metric(volume,stop_count, detector,cap,minVol,maxVol,volBar,volPer,pTime))
          print(percentage)
          cv2.VideoCapture(0).release()
          cv2.destroyAllWindows()
     elif c_fig == 2:
          ccc1 = eye.eye_detect(cap)
     elif c_fig == 3:
          ccc2= face.FaceDetection(cap)
     elif c_fig == 4:
          txt= sr.speech_rec(recognizer)
     elif c_fig == 5:
          txt=posest.estimation(cap,mpDraw,mpPose,pose,pTime)
     else:
          print('other function')

