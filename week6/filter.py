import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage


def addFilter():
    try:
        img = cv2.imread( "C://Yazilim//ImageProcessingRepository//images//Fruits.jpeg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Gaussian
        gauss = cv2.GaussianBlur(gray,(3,3),0)
        #Laplacian
        laplacian = cv2.Laplacian(gauss,cv2.CV_64F)
        #Sobel
        sobelx = cv2.Sobel(gauss,cv2.CV_64F,1,0,ksize=5)  # x
        sobely = cv2.Sobel(gauss,cv2.CV_64F,0,1,ksize=5)  # y

        #Prewitt
        kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        prewittx = cv2.filter2D(gauss, -1, kernelx)
        prewitty = cv2.filter2D(gauss, -1, kernely)
        
        #Robert Cross
        roberts_cross_v = np.array( [[ 1, 0 ], [ 0, -1 ]] )
        roberts_cross_h = np.array( [[ 0, 1 ], [ -1, 0 ]] )
        imgRobert = cv2.imread( "C://Yazilim//ImageProcessingRepository//images//Fruits.jpeg",0).astype('float64')
        imgRobert/=255.0
        vertical = ndimage.convolve( imgRobert, roberts_cross_v )
        horizontal = ndimage.convolve( imgRobert, roberts_cross_h )
        edgedRobert = np.sqrt( np.square(horizontal) + np.square(vertical))
        edgedRobert*=255
        
        # total_rows, total_columns, subplot_index(1st, 2nd, etc..)
        plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,2),plt.imshow(gray,cmap = 'gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,3),plt.imshow(laplacian,cmap = 'gray')
        plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,4),plt.imshow(gauss,cmap = 'gray')
        plt.title('Gaussian'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,5),plt.imshow(prewittx,cmap = 'gray')
        plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,6),plt.imshow(prewitty,cmap = 'gray')
        plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,7),plt.imshow(sobelx,cmap = 'gray')
        plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,8),plt.imshow(sobely,cmap = 'gray')
        plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,9),plt.imshow(edgedRobert,cmap = 'gray')
        plt.title('Robert Cross'), plt.xticks([]), plt.yticks([])

        plt.show()
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()   
             
    except KeyboardInterrupt:
        print("Kapatıldı")
