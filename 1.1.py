import cv2 as cv
import numpy as np

img = cv.imread("input/flower_input.jpg")
#img = cv.resize(img, (500,500))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

rows, cols = img.shape

# the mask and the image are blended together so that the background is blur 
# convolutional algorithme
for i in range(12, rows - 12):
    for j in range(12, cols - 12):
        if img[i, j] < 170:
            small_img = img[i-12:i+13, j-12:j+13]
            small_img_1d = small_img.reshape(625)
            small_img_1d_sorted = np.sort(small_img_1d)
            #center of reshape
            result[i, j] = small_img_1d_sorted[313]
        else:
            result[i, j] = img[i, j]


# show
cv.imwrite("output/floweroutput.jpg", result)
#cv.imshow("res", result)
cv.waitKey()