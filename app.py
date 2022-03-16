import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = cv2.imread('flower.jpg',0).astype(np.float64) 
#imread is to set const img with the image in path flower.jpg, the parameter 0 is to set the image as grayscale
#.astype to initialize the datatype of the const, in this case we set it as a float64
Kx = -1*np.array([[-1,0,1]]) #this is the kernel matrix along the x axis 
Fx = ndimage.convolve(img, Kx) #the function will convolute img and kx
cv2.waitKey(0) #waits for a key input from keyboard,
Ky = -1*np.array([[-1],[0],[1]]) #this is the kernel matrix along the y axis 
Fy = ndimage.convolve(img, Ky) 
l2 = np.sum(np.power((Fx-Fy),2)) #calculating the L2 norm      
print("The result of L2 is ",l2)
cv2.imwrite("Fx.png",np.abs(Fx)) #will create a new file that has the image of the edge processing.
                                 #note that absolute value is 
                                 #needed to disregard the sign of derivative for displaying edges
cv2.imwrite("Fy.png",np.abs(Fy))
