import cv2

def readableText():

    try:

        image = cv2.imread("C://Yazilim//ImageProcessingRepository//images//noisyText.jpeg")
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        _, result = cv2.threshold(image, 70, 100, cv2.THRESH_BINARY)

        adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 35)


        cv2.imshow("image", image)
        cv2.imshow("Result", result)
        cv2.imshow("Adaptive Result", adaptive)

        cv2.waitKey(0)
        cv2.destroyAllWindows()  

        
    except KeyboardInterrupt:
        print("Kapatıldı")

