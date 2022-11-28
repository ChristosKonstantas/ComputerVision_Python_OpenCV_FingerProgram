import cv2
import mediapipe as mp
import time


#cap = cv2.VideoCapture(0)
#pTime = 0
def estimation(cap,mpDraw,mpPose,pose,pTime):
    stop_count = 0
    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        print(results.pose_landmarks)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if results:
            stop_count = stop_count + 1

        if stop_count > 200:
            cv2.waitKey(1)
            stop_count = 0
            # print("stop")
            #cap.release()
            #cv2.destroyAllWindows()
            return 0