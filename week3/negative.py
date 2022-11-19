import cv2
import matplotlib.pyplot as plt
import numpy as np 


def negativeImage(image):

    imageNp = np.max(image)
    negative_image = imageNp - image
    return negative_image


def getNegative():

    image = cv2.imread("C://Yazilim//ImageProcessingRepository//images//grayScalingImage.jpg", 0)
    negative_image = negativeImage(image)
    together = np.hstack((image, negative_image))
    print("original image:", image.shape)
    print("negative image:", negative_image.shape)
    print("together :", together.shape)

    plt.imshow(together, cmap="gray")
    plt.show()