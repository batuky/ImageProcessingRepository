import cv2
import numpy as np

image = cv2.imread('C:\Yazilim\ImageProcessingRepository\images\Fruits.jpeg')

imageBlue = image[:,:,0]
imageGreen = image[:,:,1]
imageRed = image[:,:,2]

new_image = np.hstack((imageBlue,imageGreen,imageRed))

cv2.imshow("window",new_image)


cv2.waitKey(0)