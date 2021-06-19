import cv2
import numpy
from POSE import FindPose
from threading import *
import Tekken
import time
import pydirectinput

time.sleep(20)

def x():
	pydirectinput.press('x')
def z():
	pydirectinput.press('z')
def right():
	pydirectinput.press('left')
def left():
	pydirectinput.press('right')


cam=cv2.VideoCapture(0)
h1=FindPose()
def CameraWork():
	while True:
		_,img=cam.read()
		h,w,c=img.shape
		img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		img,angle1,angle2,knee=h1.find(img1)
		angle1,angle2=int(angle1),int(angle2)
		kneeleft=knee[0]*w
		kneeright=knee[1]*w
		# print(angle)
		img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		print(kneeleft,kneeright)
		if angle1>140 :
			t1=Thread(target=x)
			t1.start()
			# print("more than 140")
		if  angle2>140:
			t2=Thread(target=z)
			t2.start()
			# print(angle1,angle2)x
		if kneeleft<120 and kneeleft >0:
			t3=Thread(target=left)
			t3.start()
		if kneeright>500  and kneeleft <640:
			t4=Thread(target=right)
			t4.start()

		
			
		cv2.imshow("img",img1)

		if cv2.waitKey(1)==27:
			break

	cv2.destroyAllWindows()
	cam.release()

main=Thread(target=CameraWork)

main.start()
