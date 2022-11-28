import speech_recognition
import pyttsx3
import cv2



def speech_rec(recognizer):
    while True:
        stop_count = 0

        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"Recognized {text} ")
        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
            continue

        if text == "stop" :
            cv2.waitKey(1)
            stop_count = 0
            # print("stop")
            #cap.release()
            #cv2.destroyAllWindows()
            return 0
