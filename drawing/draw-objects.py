import cv2
import numpy as np

# Ein schwarzes Image erzeugen
image = np.zeros((300, 300, 3), dtype = "uint8")

# Kreis definieren
center_coordinates = (50, 50)
radius = 20
color = (255, 0, 0) # RGB-Farbe für Blau
thickness = 2

# Kreis zeichnen
image = cv2.circle(image, center_coordinates, \
    radius, color, thickness)

# Text definieren
text = 'Hallo Welt!'
point = (20, 150)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
color = (255, 0, 255) # Magenta
thickness = 3

# Text zeichnen
image = cv2.putText(image, text, point, font, \
    fontScale, color, thickness, cv2.LINE_AA)

# Bild anzeigen
cv2.imshow('Drawing', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
