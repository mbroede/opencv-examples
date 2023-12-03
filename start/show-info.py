import cv2
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\start') 

# Instanziierung eines Image-Objekts durch Einlesen 
# einer Bilddatei von der Festplatte
img_path = "2x3.bmp"
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
print("Original:\n", img)

# Pixel rechts oben grau färben
(img[0, 1]) = (127, 127, 127)
print("\nPixel rechts oben geändert:\n", img)

# Komplettes Bild in Graustufen konvertieren
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("\nGraustufen:\n", img)

# Neues Bild speichern
# cv2.imwrite('2x3_neu.bmp', img)

print("Original:\n", img)
