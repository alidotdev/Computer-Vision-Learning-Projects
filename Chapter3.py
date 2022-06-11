import cv2
import numpy as np

img = cv2.imread('Resources/lambo.PNG')
imgResize = cv2.resize(img , (1000 , 500))
imgCropped = img[0:200 , 200:500]

cv2.imshow('Image',img)
# cv2.imshow('Resized Image' , imgResize)
cv2.imshow('Cropped' , imgCropped)

print(img.shape)
print(imgResize.shape)

cv2.waitKey(0)