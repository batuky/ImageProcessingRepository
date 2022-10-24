import cv2

def method2():
    try:
        # Use the second argument or (flag value) zero
        # that specifies the image is to be read in grayscale mode
        image = cv2.imread('C:\Yazilim\ImageProcessingRepository\images\grayScalingImage.jpg', 0)
        image = cv2.resize(image,(1280,720)) 
        cv2.imshow('Grayscale Image', image)
        cv2.waitKey(0)
        
        # Window shown waits for any key pressing event
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        print("Kapatıldı")