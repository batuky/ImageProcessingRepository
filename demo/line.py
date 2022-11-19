import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os
from moviepy.editor import VideoFileClip
from IPython.display import HTML


#helper funcs are here
def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

"""
def draw_lines_m(img, lines, color=[255, 0, 0], thickness=7):
    
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    
    

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)
            
"""            
            
def draw_lines(img, lines, color=[255, 0, 0], thickness=7):
    
     #list to get positives and negatives values
    
    x_bottom_pos = []
    x_upperr_pos = []
    x_bottom_neg = []
    x_upperr_neg = []
    
    y_bottom = 540
    y_upperr = 315
    
    #y1 = slope*x1 + b
    #b = y1 - slope*x1 
    #y = slope*x + b
    #x = (y - b)/slope
    
    slope = 0
    b = 0
    
    #get x upper and bottom to lines with slope positive and negative    
    for line in lines:
        for x1,y1,x2,y2 in line:
            #test and filter values to slope
            if ((y2-y1)/(x2-x1)) > 0.5 and ((y2-y1)/(x2-x1)) < 0.8 :
                
                slope = ((y2-y1)/(x2-x1))
                b = y1 - slope*x1
                
                x_bottom_pos.append((y_bottom - b)/slope)
                x_upperr_pos.append((y_upperr - b)/slope)
                                      
            elif ((y2-y1)/(x2-x1)) < -0.5 and ((y2-y1)/(x2-x1)) > -0.8:
            
                slope = ((y2-y1)/(x2-x1))
                b = y1 - slope*x1
                
                x_bottom_neg.append((y_bottom - b)/slope)
                x_upperr_neg.append((y_upperr - b)/slope)
                
               
    #creating a new 2d array with means
    lines_mean = np.array([[int(np.mean(x_bottom_pos)), int(np.mean(y_bottom)), int(np.mean(x_upperr_pos)), int(np.mean(y_upperr))],
                           [int(np.mean(x_bottom_neg)), int(np.mean(y_bottom)), int(np.mean(x_upperr_neg)), int(np.mean(y_upperr))]])
    
    
    #Drawing the lines
    for i in range(len(lines_mean)):
        cv2.line(img, (lines_mean[i,0], lines_mean[i,1]), (lines_mean[i,2], lines_mean[i,3]), color, thickness)
                    
            
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ)

def pipeline_edges(file, 
                   kernel_size = 5, 
                   low_threshold = 50, high_threshold=150, 
                   rho=3, theta=np.pi/180, threshold=15,
                   min_line_len=100, max_line_gap=50): 
    
    #read images from files
    image = mpimg.imread('test_images/' + file)
    
    #turn in grayscale
    gray = grayscale(image)
    
    #apply blur
    blur_gray = gaussian_blur(gray, kernel_size)
    
    #finding edges
    edges = canny(image, low_threshold, high_threshold)
    
    #setting vertices
    vertices = np.array([[(0,image.shape[0]),(450, 315), (490, 315), 
                          (image.shape[1],image.shape[0])]], dtype=np.int32)
    
    #creating a region of interest
    masked_edges = region_of_interest(edges, vertices)
    
    #finding lines
    lines = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
    
    #merge with original image
    lines_edges = weighted_img(lines, image, α=0.8, β=1., λ=0.)
    
    return lines_edges


def process_image(image, 
                  kernel_size = 5, 
                  low_threshold = 100, high_threshold = 250, 
                  rho = 1, theta = np.pi/180, threshold = 30,
                  min_line_len = 100, max_line_gap = 200): 
    
    
    #turn in grayscale
    gray = grayscale(image)
    
    #apply blur
    blur_gray = gaussian_blur(gray, kernel_size)
    
    #finding edges
    edges = canny(image, low_threshold, high_threshold)
    
    #setting vertices
    vertices = np.array([[(0,image.shape[0]),(450, 315), (490, 315), 
                          (image.shape[1],image.shape[0])]], dtype=np.int32)
    
    #creating a region of interest
    masked_edges = region_of_interest(edges, vertices)
    
    #finding lines
    lines = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
    
    #merge with original image
    lines_edges = weighted_img(lines, image, α=0.8, β=1., λ=0.)
    
    return lines_edges


#reading in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')

#printing out some stats and plotting
print('This image is:', type(image), 'with dimensions:', image.shape)
plt.imshow(image)  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')

os.listdir("test_images/")

gray = grayscale(image)
plt.figure(figsize=(10,7))
plt.title("GrayScale Image")
plt.imshow(gray, cmap='gray')



kernel_size = 5 # Kernel size
blur_gray = gaussian_blur(gray, kernel_size)
plt.figure(figsize=(10,7))
plt.title("GrayScale Image with Gaussian Blur")
plt.imshow(blur_gray, cmap='gray')



low_threshold = 50
high_threshold = 150




edges = canny(blur_gray, low_threshold, high_threshold)
plt.figure(figsize=(10,7))
plt.title("Edges Detected")
plt.imshow(edges, cmap='Greys_r')



vertices = np.array([[(0,image.shape[0]),(450, 310), (490, 310), (image.shape[1],image.shape[0])]], dtype=np.int32)




mask = region_of_interest(image, vertices)
plt.figure(figsize=(10,7))
plt.title("Region of Interest")
plt.imshow(mask, cmap='Greys_r')



masked_edges = region_of_interest(edges, vertices)
plt.figure(figsize=(10,7))
plt.title("Edges on Region of Interest")
plt.imshow(masked_edges, cmap='Greys_r')



rho = 3
theta = np.pi/180
threshold = 15
min_line_len = 150
max_line_gap = 50

lines = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)




plt.figure(figsize=(10,7))
plt.title("Lines Detected")
plt.imshow(lines)



lines_edges = weighted_img(lines, image, α=0.8, β=1., λ=0.)



plt.figure(figsize=(10,7))
plt.title("Lanes detected!")
plt.imshow(lines_edges)



#read the path
path = "test_images/"
#store files names in files
files = os.listdir(path)
print(files)



images = []
for file in files:
    images.append(pipeline_edges(file, 
                                 kernel_size = 5, 
                                 low_threshold = 100, high_threshold = 250, 
                                 rho = 1, theta = np.pi/90, threshold = 30,
                                 min_line_len = 40, max_line_gap = 400))

plt.figure(figsize=(50,50))

#for each image in images create a subplot
for i in range(len(images)):
    
    indice = str(len(images)) + str(1) +str(i + 1)
    indice = int(indice)
    
    plt.subplot(indice)
    plt.title(files[i])
    plt.imshow(images[i])

    
#plot the result
plt.show()


white_output = 'test_videos_output/solidWhiteRight.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4")
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!




HTML("""

  {0}">

""".format(white_output))



yellow_output = 'test_videos_output/solidYellowLeft.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4').subclip(0,5)
clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4')
yellow_clip = clip2.fl_image(process_image)




HTML("""

  {0}">

""".format(yellow_output))

