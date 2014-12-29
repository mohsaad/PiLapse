import cv2
import os
import time

cap = cv2.VideoCapture(0)

interval = 1
duration = 10
num = 0;
currtime = 0;

while(currtime <= duration):
	[f,frame] = cap.read()
	if f == False:
		break
	name = str(num) + '.png'
	cv2.imwrite(name, frame)

	#if ch == 27:
	#	break

	num += 1
	currtime += interval
	time.sleep(interval)


cap.release()

cv2.destroyAllWindows()