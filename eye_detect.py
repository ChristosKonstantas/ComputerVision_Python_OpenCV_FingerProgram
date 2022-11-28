import numpy as np
import cv2

def eye_detect(cap):
    stop_count = 0

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.15, 7)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.15, 7)
            print (roi_color)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

        if len(eyes) == 0:
            stop_count = stop_count + 1
            print(stop_count)

        if stop_count > 100:
            cv2.waitKey(1)
            # print("stop")
            #cap.release()
            #cv2.destroyAllWindows()
            return 0
