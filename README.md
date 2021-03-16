# Dullrazor algorithm 💻🧬

<img src="screenshots/screenshot_0.png" alt="homepage"><br>
<hr>

### Minimum requirements 

<p>Programming language: <i>Python</i><br>
Version language: <i>Python 3.8.8</i><br>
Libraries: <i>OpenCV 4.5.1</i><br>
</p>
<hr>

<p style="text-align:justify;">Most images of skin lesions have unwanted elements, such as shadows and hairs, which can make it difficult to segment the lesion and introduce erroneous information on its characteristics. Therefore, it is necessary to apply some artificial vision techniques to eliminate any noise component.</p>

<p style="text-align:justify;">Body hair is one of the factors that can affect lesion segmentation. For the detection and removal of hairs, a pre-processing technique called DullRazor is used, which consists of applying a series of morphological operations to the image in order to generate a mask that contains the hairs. The steps to apply the DullRazor algorithm are:</p>

<ol>
    <li>Convert the original image to grayscale.</li>
    <li>Closing to the grayscale image, using a linear or cross-shaped kernel.</li>
    <li>Calculate the difference between the resulting image and the original.</li>
    <li>Apply binary thresholding to obtain a mask with the hairs in the image.</li>
    <li>Replace the pixels in common between the mask and the original image, with pixels from the latter.</li>
</ol>
<p>For steps 2 and 3 of the DullRazor algorithm, the advanced morphological operation blackhat from the OpenCV library was used. On the other hand, the cv2.inpaint command from the same library was used in the last step of the algorithm.</p>
<hr>

## SCREENSHOTS

<p>Input image from HAM10000 database.</p>

### Input image
<img src="screenshots/screenshot_1.png" alt="Input image"><br>

### Cropped image
<img src="screenshots/screenshot_2.png" alt="Cropped image"><br>

### Gray scale image
<img src="screenshots/screenshot_3.png" alt="Gray scale image"><br>

### Black hat filter
<img src="screenshots/screenshot_4.png" alt="Black hat filter"><br>

### Binary Thresholding (Mask)
<img src="screenshots/screenshot_5.png" alt="Binary Thresholding"><br>

### Replace pixels of the mask (Output image)
<img src="screenshots/screenshot_6.png" alt="Output image"><br>

<p><i>Developed by engineer Javier Velasquez (2020)</i></p>
