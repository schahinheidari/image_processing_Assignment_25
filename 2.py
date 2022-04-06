import cv2 as cv
import numpy as np

img = cv.imread("input/lion.png")
img = cv.resize(img, (400,400))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

res = np.zeros(img.shape)
rows, cols = img.shape
filter = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])


for i in range(2, rows - 2):
    for j in range(2, cols - 2):
        smallImg = img[i-1:i+2, j-1:j+2] # (3*3)
        #smallImg = img[i-2:i+3, j-2:j+3] # (5*5)
        res[i][j]= np.sum(smallImg * filter)
        
cv.imwrite("output/lionResult.jpg", res)
cv.imshow("show", res)
cv.waitKey() 