import cv2
import os
import time

cap = cv2.VideoCapture(0)

height = 1280
width = 720

[exf, exframe1] = cap.read()
if exf == True:
	[height, width, layets] = exframe1.shape
	cv2.imwrite('eximage.png', exframe1)

print width
print height
interval = 1
duration = 100
num = 0;
currtime = 0;

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
outvid = cv2.VideoWriter('lapse.avi', 0,10, (width,height))

while(currtime <= duration):
	[f,frame] = cap.read()
	if f == False:
		break

	outvid.write(frame)

	#if ch == 27:
	#	break
	#print num
	num += 1
	currtime += interval
	time.sleep(interval)


cap.release()
cv2.destroyAllWindows()