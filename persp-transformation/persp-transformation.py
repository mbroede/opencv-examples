import cv2
import numpy as np
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\persp-transformation') 

# Bild laden
img = cv2.imread(r'image.png', cv2.IMREAD_UNCHANGED)

# Quell- und Zielkoordinaten festlegen
breite = 450
hoehe = 600
src_pts = np.float32([[0, 0], [breite, 0], [breite, hoehe], [0, hoehe]])
dst_pts = np.float32([[0 - 100, 0 + 100], [breite + 50, 0 - 50], [breite, hoehe], [0, hoehe]])

# Transformationsmatrix erstellen
M = cv2.getPerspectiveTransform(src_pts, dst_pts)

# Transformationsmatrix anwenden
transformed_img = cv2.warpPerspective(img, M, (breite, hoehe))

cv2.imshow('transform', transformed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
