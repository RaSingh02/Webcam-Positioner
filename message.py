from gtts import gTTS #gTTS
import os
import pyaudio #pyaudio
import math
import speech_recognition as sr #speech_recognition
import cv2 #OpenCV
import sys
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
img_counter = 0

# Initializing the "specifiy location" tts
text = "Which quadrant would you like to be in? Specify top left, top right, bottom left, or bottom right."
tts = gTTS(text)
tts.save("init.mp3")
os.system("init.mp3")

# Check that the speech to text converts correctly   
ask_quadrant = sr.Recognizer()
with sr.Microphone() as source:
        sleep(8)
        audio = ask_quadrant.listen(source)
        text = "We are lining up the image for " + ask_quadrant.recognize_google(audio) 
        tts = gTTS(text)
        tts.save("file.mp3")
        os.system("file.mp3")
        sleep(3.75)

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)

    #Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Finding the face in the frame
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        
        #Center of Rectangle Calculation:
        center_x = math.floor(x + (w/2))
        center_y = math.floor(y + (h/2))

        #Center of Frame Calculations:
        h, w, _ = frame.shape
        center_w = math.floor(w/2)
        center_h = math.floor(h/2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    #Directions for Top-Left Quadrant
    if (ask_quadrant.recognize_google(audio) == "top left"):
        if (center_x > center_w):
            text = "Move to your left."
            tts = gTTS(text)
            tts.save("Left.mp3")
            os.system("Left.mp3")
        elif (center_y > center_h):
            text = "Move up."
            tts = gTTS(text)
            tts.save("Up.mp3")
            os.system("Up.mp3")
        else:
            text = "Please remain still for the capture."
            tts = gTTS(text)
            tts.save("Capture.mp3")
            os.system("Capture.mp3")
            sleep(3)
            if img_counter != 1:
                img_name = "NewPicture.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                ++img_counter
            text = "Image Captured"
            tts = gTTS(text)
            tts.save("Taken.mp3")
            os.system("Taken.mp3")
            break
        sleep(3.75)
    #Directions for Top-Right Quadrent 
    elif (ask_quadrant.recognize_google(audio) == "top right"):
        if (center_x < center_w):
            text = "Move to your right."
            tts = gTTS(text)
            tts.save("Right.mp3")
            os.system("Right.mp3")
        elif (center_y > center_h):
            os.system("Up.mp3")
        else:
            os.system("Capture.mp3")
            sleep(3)
            if img_counter != 1:
                img_name = "NewPicture.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                ++img_counter
            os.system("Taken.mp3")
            break
        sleep(3.75)
    #Directions for Bottom Left Quadrent
    elif (ask_quadrant.recognize_google(audio) == "bottom left"):
        if (center_x > center_w):
            os.system("Left.mp3")
        elif (center_y < center_h):
            text = "Move down."
            tts = gTTS(text)
            tts.save("Down.mp3")
            os.system("Down.mp3")
        else:
            os.system("Capture.mp3")
            sleep(3)
            if img_counter != 1:
                img_name = "NewPicture.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                ++img_counter
            os.system("Taken.mp3")
            break
        sleep(3.75)
    #Directions for Bottom Right Quadrent
    elif (ask_quadrant.recognize_google(audio) == "bottom right"):
        if (center_x < center_w):
            os.system("Right.mp3")
        elif (center_y < center_h):
            text = "Move down."
            tts = gTTS(text)
            tts.save("Down.mp3")
            os.system("Down.mp3")
        else:
            os.system("Capture.mp3")
            sleep(3)
            if img_counter != 1:
                img_name = "NewPicture.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                ++img_counter
            os.system("Taken.mp3")
            break
        sleep(3.75)
    else:
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()