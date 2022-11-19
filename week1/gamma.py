import cv2
import numpy as np


def gammaTransection():
    img = cv2.imread("C://Yazilim//ImageProcessingRepository//images//Fruits.jpeg")

    for gamma in [3.0, 4.0, 5.0]:
        gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
        cv2.imshow("a", gamma_corrected)
        cv2.waitKey(0)
    cv2.destroyAllWindows()