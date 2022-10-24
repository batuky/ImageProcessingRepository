import cv2
 
def method3():
    try:
        # Load the input image
        image = cv2.imread('C:\Yazilim\ImageProcessingRepository\images\grayScalingImage.jpg')
        image = cv2.resize(image,(1280,720)) 
        # Obtain the dimensions of the image array
        # using the shape method
        (row, col) = image.shape[0:2]
        
        # Take the average of pixel values of the BGR Channels
        # to convert the colored image to grayscale image
        for i in range(row):
            for j in range(col):
                # Find the average of the BGR pixel values
                image[i, j] = sum(image[i, j]) * 0.33
        
        cv2.imshow('Grayscale Image', image)
        cv2.waitKey(0)
        
        # Window shown waits for any key pressing event
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        print("Kapatıldı")