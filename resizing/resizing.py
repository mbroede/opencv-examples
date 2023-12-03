import cv2
import numpy as np
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\resizing') 

# Bild laden
image = cv2.imread('image_300x225.jpg', cv2.IMREAD_UNCHANGED)

# Verschiedene Größen
half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
bigger = cv2.resize(image, (900, 675))
interpol = cv2.resize(image, (900, 675), 
                      interpolation = cv2.INTER_LANCZOS4)
images = [image, half, bigger, interpol]

# Verschiedene Titel
titles = ["original", "half", "bigger", "interpol"]

# Anzeige
for i in range(len(images)):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

