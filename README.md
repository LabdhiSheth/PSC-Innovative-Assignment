# What is Image Segmentation?

The first step towards understanding Image Segmentation lies in understanding the meaning of the term pixels. Pixels are essentially coloured “points” that make up a larger image. The term is used in a digital reference. 

Image Segmentation, therefore, as the name suggests, is the segmentation, or division, of an image into parts. Each of these segments, thus, represent a part of that image and so, cover it.



# Why do we need Image Segmentation?

Image Segmentation comes into use when images are to be analysed. Its main goal is to represent an image as something more meaningful and easier to analyse. It finds applications in healthcare industries, autonomous driving, face detection, number plate detection, video surveillance, detecting objects in satellite images etc., which makes it an invaluable field of knowledge in today’s world.



# Region-Based Segmentation

One of the techniques of carrying out image segmentation, is through region-based image segmentation. The key terms to keep in mind in this method are pixel values and threshold values.

A pixel value is a number related to a particular pixel that represents its “brightness”. Pixels of an image are allocated into different classes (or regions) depending on a threshold value. This is an imaginary line, of sorts, for pixel values. If a pixel value is above the threshold value, it is classified as an object, and if it is lower, it is classified as a background. In this case, where there is only a background and an object, i.e., when there are only two regions, the threshold value is referred to as the global threshold. However, not all images in the world can be classified as such. Usually, images have more than just one object, and therefore, a single threshold value is not enough. In such a case, multiple threshold values are defined, which collectively, are called the local threshold.

This method of region-based image segmentation works best when the objects and background of the image have a high contrast. And so, it is understandable that this method comes with its set of limitations. 



# Edge Detection
	
An edge is an abrupt change or transition in the intensity of pixels. They usually occur on the boundary of two regions.

Edge Detection, therefore, is an image processing technique that deals with the ‘detection’ of these edges. It contains a range of mathematical methods that aims at identifying edges (or points) in an image which changes the image brightness sharply.

There are three types of edges - horizontal, vertical and diagonal.


# Why Detect Edges?

An edge contains most of the information about shape. Hence, we detect and use filters to make the image more clear.
 

# Applications of Edge Detection

●	Extracting important features of an image. (Detecting an edge leads to doing away with much of the detail, thus making the image more lightweight.)

●	Increasing sharpness and making images clearer.

●	Recognizing objects, boundaries and segmentation.




# Different Methods of Edge Detection

1.	First Order Derivative (Gradient Method)
	
This is the most common method used. It uses gradient operators and is best suited for abrupt discontinuities.
Mathematically the image function, magnitude (strength of the edge) and direction (opposite of the edge direction) are computed as 
					|⛛L| = √ (L2x + L2y)
		and,
					θ = atan2(Ly, Lx).

Another simple implementation would be to combine the following mentioned mask and image data - which has the capability of detecting edges and their direction but are sensitive to noise and not accurate in locating edges.
		

2.	Second Order Derivative (Zero-Crossing Method)

This method captures the rate of change in the intensity of the gradient, and thus, detection of the zero-crossings captures the local maxima in the gradient. 
The steps are smoothed by a Gaussian filter, edges are enhanced using Laplacian operators, and Linear Interpolation is used for determining the location of sub pixels of the edge. 
It is cheaper to implement as we combine two filters in one but it does not provide information on direction. There’s a probability of false and missing edges.



# Masks for Edge Detection

❏	Prewitt Operator
This is used for detection of horizontal and vertical edges.

❏	Sobel Operator
Prewitt and Sobel are close as Sobel, too, calculates edges in both the horizontal and vertical directions.

❏	Robinson Compass
This is a direction mask which computes edges for all eight major directions.

❏	Laplacian Operator 
This second order derivative mask is used to compute edges in an image and can be further divided into positive and negative.


# Conclusion

In conclusion, Image Segmentation is a process of dividing images into various segments that help ultimately in detecting various objects and the background in that image. 

Region-Based Image Segmentation and Edge Detection are two amongst the various methods of Image Segmentation. Region based segmentation deals with pixel and threshold values that help in detecting whether a pixel belongs to the ‘background’ class or the ‘object’ class. The Edge Detection method deals with detecting the abrupt changes in the intensity of the pixels and the information of shapes made by the pixels.

Image Segmentation finds its applications in important aspects such as healthcare, security and evolving technology, and has thus become an invaluable field of knowledge.

