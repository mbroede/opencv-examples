# Ermittlung von Eigenschaften der angeschlossenen WebCam
import cv2
import os

os.chdir(r'c:\projects\py\opencv-examples\system') 

cap = cv2.VideoCapture(0) 
while cap.isOpened(): 
	_, frame = cap.read() 
	cv2.imshow('webcam', frame) 

	if cv2.waitKey(1) & 0xff == 27:
		break

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print(width, height, fps)

cap.release()								 
cv2.destroyAllWindows() 

