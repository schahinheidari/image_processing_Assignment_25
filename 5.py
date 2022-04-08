import cv2
import numpy as np

img = cv2.imread("input/1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numInput = int(input("Choose and input one of the number like 3 - 5 - 7 - 9 - 25 - 49 - 225: "))

def convolution(img, numInput, shape):
    print(numInput)
    rows, cols = shape
    res = np.zeros(img.shape)
    mask = np.ones((numInput, numInput)) / (numInput * numInput)

    for i in range((numInput // 2), rows - (numInput // 2)):
        for j in range((numInput // 2), cols - (numInput // 2)):
            smallImg = img[i - (numInput // 2) : i + (numInput // 2) + 1, j - (numInput // 2) : j + (numInput // 2) + 1]
            res[i, j] = np.sum(smallImg * mask)
            
    return res



res = convolution(img, numInput, img.shape)       
cv2.imwrite("output/conv7.jpg", res)