import cv2
import time
import os
import HandTrackingModule as htm

#wCam, hCam = 640, 480

#cap = cv2.VideoCapture(1)

#cap.set(3, wCam)
#cap.set(4, hCam)

#detector = htm.handDetector(detectionCon=0.75)
#tipIds = [4, 8, 12, 16, 20]

#stop_count = 0

def counterFunc(stop_count, tipIds, detector,cap):
    fig = 0
    while True :
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        fingers1 = []
        fingers2 = []

        for i in range (len(lmList)):

            if lmList[i][0][1] < lmList[i][1][1]:

                if (lmList[i][tipIds[0]][1] > lmList[i][tipIds[0] - 1][1]):
                    fingers1.append(1)
                else:
                    fingers1.append(0)

                for id in range(1, 5):
                    if lmList[i][tipIds[id]][2] < lmList[i][tipIds[id] - 2][2]:
                        fingers1.append(1)
                    else:
                        fingers1.append(0)

            if lmList[i][0][1] > lmList[i][1][1]:

                if (lmList[i][tipIds[0]][1] < lmList[i][tipIds[0] - 1][1]):
                    fingers2.append(1)
                else:
                    fingers2.append(0)

                for id in range(1, 5):
                    if lmList[i][tipIds[id]][2] < lmList[i][tipIds[id] - 2][2]:
                        fingers2.append(1)
                    else:
                        fingers2.append(0)

        #print(fingers2, fingers1)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

        if len(lmList) != 0:
            fig = sum(fingers1) + sum(fingers2)

        if len(lmList) != 0:
            stop_count = stop_count + 1
            #print(stop_count)

        if stop_count > 100:
            cv2.waitKey(1)
            stop_count = 0
            #print("stop")
            return fig