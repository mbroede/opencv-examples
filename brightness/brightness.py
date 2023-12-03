import cv2
import numpy as np
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\brightness') 

# Bild laden
image = cv2.imread('image.png')

# Helligkeitswert vorgeben
brightness = 42

# Array mit der gleichen Form wie das Bild, 
# aber mit dem Helligkeitswert gefüllt
arr = np.full(image.shape, brightness, dtype=np.uint8)

# Helligkeitswerte zum Bild hinzufügen
brighter_image = cv2.add(image, arr)

# Anzeige
cv2.imshow('original', image)
cv2.imshow('brighter', brighter_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
