import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')


imghor = np.hstack((img,img))
imgver = np.vstack((img, img))
cv2.imshow('Image' , imghor)
cv2.imshow('Vertical Image' , imgver)



cv2.waitKey(0)