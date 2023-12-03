import cv2
import numpy as np
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\outline-detection') 

# Bild laden
filename = "image_outlines.jpg"
image = cv2.imread(filename, cv2.IMREAD_COLOR)
image_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) 

# Umwandlung des Grau-Bildes in ein Binärbild (schwarzweiß)
_, threshold = cv2.threshold(image_gray, 110, 255, cv2.THRESH_BINARY) 

# Konturen suchen
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, 
							   cv2.CHAIN_APPROX_SIMPLE) 

# Treffer markieren
for i in range(1, len(contours)):
	cv2.drawContours(image, [contours[i]], 0, (0, 0, 255), 5)

# Anzeige
if len(contours) > 0:
	cv2.imshow('original', cv2.imread(filename, cv2.IMREAD_COLOR)) 
	cv2.imshow('result', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


