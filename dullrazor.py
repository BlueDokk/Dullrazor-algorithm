# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:42:26 2020

@author: Javier Velasquez P.
"""   
import cv2

#IMAGE ACQUISITION

#Input image
path='ISIC_0031023.jpg'
#Read image
image=cv2.imread(path,cv2.IMREAD_COLOR)
#Image cropping
img=image[30:410,30:560]
    
#DULL RAZOR (REMOVE HAIR)

#Gray scale
grayScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY )
#Black hat filter
kernel = cv2.getStructuringElement(1,(9,9)) 
blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
#Gaussian filter
bhg= cv2.GaussianBlur(blackhat,(3,3),cv2.BORDER_DEFAULT)
#Binary thresholding (MASK)
ret,mask = cv2.threshold(bhg,10,255,cv2.THRESH_BINARY)
#Replace pixels of the mask
dst = cv2.inpaint(img,mask,6,cv2.INPAINT_TELEA)   

#Display images
cv2.imshow("Original image",image)
cv2.imshow("Cropped image",img)
cv2.imshow("Gray Scale image",grayScale)
cv2.imshow("Blackhat",blackhat)
cv2.imshow("Binary mask",mask)
cv2.imshow("Clean image",dst)

cv2.waitKey()
cv2.destroyAllWindows()
    
    
    