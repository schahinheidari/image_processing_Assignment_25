import cv2 as cv

import numpy as np

img = cv.imread("input/flower_input.jpg")
img = cv.resize(img, (500,500))

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
biggestContours = None
biggestArea = 0
for c in contours:
    area = cv.contourArea(c)
    if area > biggestArea:
        biggestArea = area
        biggestContours = c

# draw contours
cropMask = np.zeros_like(mask)
cv.drawContours(cropMask, [biggestContours], -1, (255), -1)

# fill in holes
# inverted
inverted = cv.bitwise_not(cropMask)

# contours again
contours, _ = cv.findContours(inverted, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# find small contours
smallContours = []
for c in contours:
    area = cv.contourArea(c)
    if area < 25000:
        print(area)
        smallContours.append(c)

# draw on mask
cv.drawContours(cropMask, smallContours, -1, (255), -1)

# opening + median blur to smooth jaggies
pieceChoosedMask = cv.erode(cropMask, kernel, iterations = 1)
pieceChoosedMask = cv.dilate(pieceChoosedMask, kernel, iterations = 1)
pieceChoosedMask = cv.medianBlur(pieceChoosedMask, 5)

# crop image
crop = np.zeros_like(img)
crop[pieceChoosedMask == 255] = img[pieceChoosedMask == 255]

# show
cv.imshow("cropped", crop)
cv.waitKey()