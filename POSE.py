import cv2
import mediapipe as mp
import numpy as np
# Manav Rao 6-19-2021 ------------
class FindPose():
	def __init__(self):
		self.pose1=mp.solutions.pose
		self.pose=self.pose1.Pose()
		self.draw=mp.solutions.drawing_utils
	

	def find(self,img):
		result=self.pose.process(img)
		def angle(a,b,c):
			# finding angle 
			a = np.array(a) 
			b = np.array(b) 
			c = np.array(c) 
			radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
			angle = np.abs(radians*180.0/np.pi)

			if angle >180.0:
			    angle = 360-angle
			    
			return angle
		if result.pose_landmarks:
			self.draw.draw_landmarks(img,result.pose_landmarks,self.pose1.POSE_CONNECTIONS)
			land=result.pose_landmarks.landmark
			# kneeleft=land[26].x
			# kneeright=land[25].x
			knee=[land[26].x,land[25].x]
			sholder=[land[12].x,land[12].y]
			elbow=[land[14].x,land[14].y]
			wrist=[land[16].x,land[16].y]

			sholder1=[land[11].x,land[11].y]
			elbow1=[land[13].x,land[13].y]
			wrist1=[land[15].x,land[15].y]

			return img,angle(sholder,elbow,wrist),angle(sholder1,elbow1,wrist1),knee
		else:
			return img,-1,-1,[-1,-1]
			

