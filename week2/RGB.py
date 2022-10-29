import cv2

def rgbToBgr():
    try:
        image = cv2.imread("C:\Yazilim\ImageProcessingRepository\images\elma.jpg")
        
        # converting BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image_rgb = cv2.resize(image_rgb,(1280,720))  
        cv2.imshow('image', image_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except KeyboardInterrupt:
        print("Kapatıldı")