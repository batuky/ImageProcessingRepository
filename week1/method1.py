import cv2
 
def method1(): 
    try:
        # Load the input image
        image = cv2.imread('C:\Yazilim\ImageProcessingRepository\images\grayScalingImage.jpg')
        #resize the input image
        image = cv2.resize(image,(1280,720))
        #firstly shows original image
        cv2.imshow('Original', image)
        cv2.waitKey(0)

        # Use the cvtColor() function to grayscale the image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.resize(gray_image,(1280,720)) 
        #secondly shows gray image
        cv2.imshow('Grayscale', gray_image)
        cv2.waitKey(0) 

        # Window shown waits for any key pressing event
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        print("Kapatıldı")