import cv2
import sys
from time import sleep
import math
import speech_recognition as sr
import logging as log
import datetime as dt

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

#Ask for area of screen    
ask_quadrant = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!") # Change to text-to-speech
    audio = ask_quadrant.listen(source)
try:
    print("Google Speech Recognition thinks you said " + ask_quadrant.recognize_google(audio)) #Replace with speech back to user
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio") #Replace with speech back to user
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) #Replace with speech back to user

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #Center of circle calculations
        x_1 = w/2
        x_2 = math.floor(x + x_1)
        y_1 = h/2
        y_2 = math.floor(y + y_1)

        #Center of frame calculations
        h, w, _= frame.shape
        center_w = math.floor(w/2)
        center_h = math.floor(h/2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows