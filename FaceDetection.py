import cv2
import mediapipe as mp
import time


def FaceDetection(cap):
    #cap=cv2.VideoCapture(0)
    pTime=0
    stop_count = 0

    mpFaceDetect= mp.solutions.face_detection
    mpDrawing= mp.solutions.drawing_utils

    faceDetection=mpFaceDetect.FaceDetection()

    while True:
        success, img = cap.read()

        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results= faceDetection.process(imgRGB)
        print(results)

        if results.detections:
            for id,detection in enumerate(results.detections):
                mpDrawing.draw_detection(img,detection)
                print(id,detection)
                print("This is a face with a probability",detection.score)



        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        if len(results.detections) != 0:
            stop_count = stop_count + 1
            print(stop_count)

        if stop_count > 100:
            cv2.waitKey(1)
            stop_count = 0
            # print("stop")
            #cap.release()
            #cv2.destroyAllWindows()
            return 0
