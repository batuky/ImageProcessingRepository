import cv2
import matplotlib.pyplot as plt
import numpy as np 


def negativeConversion(image):
    img=np.max(image)
    negative_image = img - image
    return negative_image

image = cv2.imread("C:/Yazilim/ImageProcessingRepository/images/Fruits.jpeg",0)
negative_image= negativeConversion(image)
together = np.hstack((image, negative_image))

print("orginal : ", image.shape)
print("negative : ", negative_image.shape)
print("together : ", together.shape)

plt.imshow(together, cmap="gray")
plt.show()