import cv2
import numpy as np
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\gamma') 

# Bild laden
image = cv2.imread('image.png')

# Gamma-Wert, wenn < 1 dann heller, wenn > 1 dann dunkler
gamma = 3.0

# Array mit vorberechneten Gamma-Werten erstellen
invGamma = 1 / gamma
arr = [((i / 255) ** invGamma) * 255 for i in range(256)]
arr = np.array(arr, np.uint8)

# Lookup-Tabelle (LUT) erzeugen
imageGamma = cv2.LUT(image, arr)

# Anzeige
cv2.imshow('original', image)
cv2.imshow('gamma', imageGamma)

cv2.waitKey(0)
cv2.destroyAllWindows()

