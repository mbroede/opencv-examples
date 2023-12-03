import numpy as np
import cv2
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\shearing-transformation') 

# Bild laden
img = cv2.imread(r'sudoku.jpg')

rows, cols = img.shape[:2]

# Shearing-Transformationsmatrix erstellen
M = np.float32([[1, 0.5, 0], [0,  1, 0]])

# Shearing-Transformation anwenden
sheared_img = cv2.warpAffine(img, M, (int(cols*1.5), rows))

# Ergebnis anzeigen
cv2.imshow('Shearing transformation', sheared_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
