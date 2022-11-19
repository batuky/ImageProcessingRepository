import cv2
import matplotlib.pyplot as plt
import numpy as np


def logTransformation():
    image = cv2.imread("C://Yazilim//ImageProcessingRepository//images//grayScalingImage.jpg")

    c= 255/np.log(1+np.max(image))
    log_image = c * (np.log(image+1))

    log_image = np.array(log_image, dtype = np.uint8)

    plt.imshow(image)
    plt.show()
    plt.imshow(log_image)
    plt.show()
