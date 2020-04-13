#                               PSC Innovative Assignment
#Project title - Image Segmentation using Region based and Edge based segmentation
#Roll numbers - 18bce101,18bce098,18bce099

#importing all the required libraries
from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

#REGION BASED SEGEMNTATION

image = cv2.imread('cancer_cells.jpg')                                            #reading the image using cv2
cv2.imshow('Original image',image)
cv2.waitKey(5000)
cv2.destroyWindow('Original image')

gray_image = rgb2gray(image)                                                       #converting to gray scale
cv2.imshow('Gray image',gray_image)
cv2.waitKey(5000)
cv2.destroyWindow('Gray image')

print("Height and width of the image in pixels are : ",gray_image.shape)
gray_threashold = gray_image.reshape(gray_image.shape[0]*gray_image.shape[1],1)
print("List of the pixel values are : ",gray_threashold)
print("Mean of the gray scale image : ",gray_image.mean())

for i in range(gray_threashold.shape[0]):                                               #gray_threashold.shape covers the whole image here 50496 pixels
    if(gray_threashold[i] > gray_image.mean()):
        gray_threashold[i] = 1                                                          #object
    else:
        gray_threashold[i] = 0                                                          #background

threashold_image = gray_threashold.reshape(gray_image.shape[0], gray_image.shape[1])
cv2.imshow("Threshold image",threashold_image)
cv2.waitKey(5000)
cv2.destroyWindow('Threshold image')

#EDGE BASED SEGMENTATION

#1. Using sobel operator
sobel_horizontal = np.array([np.array([1,2,1]),np.array([0,0,0]),np.array([-1,-2,-1])])         #weights for horizontal edges
sobel_vertical = np.array([np.array([-1,0,1]),np.array([-2,0,2]),np.array([-1,0,1])])           #weights for vertical edges

sobel_h = ndimage.convolve(gray_image,sobel_horizontal)
cv2.imshow('Sobel - Horizontal edges',sobel_h)

sobel_v = ndimage.convolve(gray_image,sobel_vertical)
cv2.imshow('Sobel - Vertical edges',sobel_v)

cv2.waitKey(5000)
cv2.destroyWindow('Sobel - Horizontal edges')
cv2.destroyWindow('Sobel - Vertical edges')

#2. Using prewitt operator
prewitt_horizontal = np.array([np.array([-1,-1,-1]),np.array([0,0,0]),np.array([1,1,1])])         #weights for horizontal edges
prewitt_vertical = np.array([np.array([-1,0,1]),np.array([-1,0,1]),np.array([-1,0,1])])           #weights for vertical edges

pre_h = ndimage.convolve(gray_image,prewitt_horizontal)
cv2.imshow('Prewitt - Horizontal edges',pre_h)

pre_v = ndimage.convolve(gray_image,prewitt_vertical)
cv2.imshow('Prewitt - Vertical edges',pre_v)

cv2.waitKey(5000)
cv2.destroyWindow('Prewitt - Horizontal edges')
cv2.destroyWindow('Prewitt - Vertical edges')

#3. Using roberts operator
roberts_horizontal = np.array([np.array([1,-0]),np.array([0,-1])])                   #weights for horizontal edges
roberts_vertical = np.array([np.array([0,1]),np.array([-1,0])])                      #weights for vertical edges

roberts_h = ndimage.convolve(gray_image,roberts_horizontal)
cv2.imshow('Roberts - Horizontal edges',roberts_h)

roberts_v = ndimage.convolve(gray_image,roberts_vertical)
cv2.imshow('Roberts - Vertical edges',roberts_v)

cv2.waitKey(5000)
cv2.destroyWindow('Roberts - Horizontal edges')
cv2.destroyWindow('Roberts - Vertical edges')

#4 Canny edge detection - on the image
original_image = cv2.imread('cancer_cells.jpg',0)
canny = cv2.Canny(original_image,100,200)
cv2.imshow('Canny edge Detection',canny)
cv2.waitKey(5000)
cv2.destroyWindow('Canny edge Detection')

#5 Canny edge detection using video
live = cv2.VideoCapture(0)                                           #return video from the webcam on your computer

while True:
    ignored, frame = live.read()                                      #tuple returned from cap.read() is being unpacked into the two variables _ and frame
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_video, 60, 300)
    cv2.imshow("Canny edge Detection", edges)
    cv2.imshow("Gray video", gray_video)
    if cv2.waitKey(1) == ord("q"):                                    #press q to exit
        break

live.release()
cv2.destroyWindow("Canny edge Detection")

