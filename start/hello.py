import cv2
import os

# Arbeitsverzeichnis einstellen
os.chdir(r'c:\projects\py\opencv-examples\start') 

# Instanziierung eines Image-Objekts durch Einlesen 
# einer Bilddatei von der Festplatte
img_path = "hello.jpg"
img = cv2.imread(img_path, cv2.IMREAD_ANYCOLOR)

# Anzeige des Images in einem eigenen Fenster
window_name = "hello world"
cv2.imshow(window_name, img)

# Auf beliebigen Tastendruck warten
cv2.waitKey(0)

# Fenster schließen und Speicher freigeben
cv2.destroyAllWindows()
