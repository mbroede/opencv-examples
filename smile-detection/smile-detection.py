import cv2
import numpy as np
import os

# Arbeitsverzeichnis für Skript und xml-Files einstellen
os.chdir(r'c:\projects\py\opencv-examples\smile-detection') 

# Machine-Learning-Modelle, Quelle: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml') 

# Liefert den übergebenen Frame mit einem blauen Rechteck um das Gesicht (sofern 
# gefunden) und ein rotes Rechteck um ein gefundenes Lächeln.
def detect(gray, frame): 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
	for (x, y, w, h) in faces: 
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
		roi_gray = gray[y:y + h, x:x + w] 
		roi_color = frame[y:y + h, x:x + w] 
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 
		for (sx, sy, sw, sh) in smiles: 
			cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
	return frame 

# Ausgabe definieren
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# Stream von der WebCam entgegennehmen und Frame für Frame auswerten
video_capture = cv2.VideoCapture(0) 
while video_capture.isOpened(): 
	_, frame = video_capture.read() 

	# Jedes Bild wird in Graustufen umgewandelt, ausgewertet und angezeigt
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
	canvas = detect(gray, frame) 
	cv2.imshow('please smile', canvas)

	# Frame speichern
	out.write(canvas) 

	# ESC beendet die Schleife
	if cv2.waitKey(1) & 0xff == 27:			 
		break

# Ressourcen freigeben
video_capture.release()								 
cv2.destroyAllWindows() 


# Orginal siehe: https://www.geeksforgeeks.org/python-smile-detection-using-opencv/
