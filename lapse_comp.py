import cv2
import os
import time

cap = cv2.VideoCapture(0);
obj = 1

while(True):
	[f,frame] = cap.read()
	if f == False:
		break

	frame = cv2.resize(frame, (640,480))
	cv2.imshow('Video', frame)
	ch = cv2.waitKey(20)

	if ch == 27:
		break

cap.release()

cv2.destroyAllWindows()