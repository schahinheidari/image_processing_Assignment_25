import cv2 as cv

import numpy as np

img = cv.imread("image_processing_Assignment_25/input/flower_input.jpg")
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.resize(img, (500,500))
#img = cv.medianBlur(img, 15)
#img = cv.bilateralFilter(img, 5, 100, 100)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# canny
canned = cv.Canny(gray, 100, 200)

# dilate to close holes in lines
kernel = np.ones((3,3),np.uint8)
mask = cv.dilate(canned, kernel, iterations = 1)

# find contours
contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# find big contours
biggesContours = None
biggestArea = 0
for contour in contours:
    area = cv.contourArea(contour)
    if area > biggestArea:
        biggestArea = area
        biggesContours = contour

# draw contours
cropMask = np.zeros_like(mask)
cv.drawContours(cropMask, [biggesContours], -1, (255), -1)

# fill in holes
# inverted
inverted = cv.bitwise_not(cropMask)

# contours again
contours, _ = cv.findContours(inverted, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# find small contours
smallContours = []
for contour in contours:
    area = cv.contourArea(contour)
    if area < 25000:
        print(area)
        smallContours.append(contour)

# draw on mask
cv.drawContours(cropMask, smallContours, -1, (255), -1)

# opening + median blur to smooth jaggies
pieceChoseMask = cv.erode(cropMask, kernel, iterations = 1)
pieceChoseMask = cv.dilate(pieceChoseMask, kernel, iterations = 1)
pieceChoseMask = cv.medianBlur(pieceChoseMask, 5)

# crop image
crop = np.zeros_like(img)
crop[pieceChoseMask == 255] = img[pieceChoseMask == 255]

# show
#cv.imshow("original", img)
#cv.imshow("gray", gray)
#cv.imshow("canny", canned)
#cv.imshow("mask", crop_mask)
cv.imshow("cropped", crop)
cv.waitKey()