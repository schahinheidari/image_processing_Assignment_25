import numpy as np
import cv2 as cv

cap = cv.VideoCapture(-1)
font = cv.FONT_ITALIC
fontSize = 1
textColor = (0, 0, 0)
thickness = 1

while True:

    ret, frame = cap.read()
    frame = cv.resize(frame,(500,500), fx = 0, fy = 0, interpolation=cv.INTER_CUBIC)
    filter = np.ones((50,50))/ 2500
    cv.rectangle(frame, (200,200), (300,300), (0,0,0), 4)
    point = frame[200:300, 200:300]
    
    res = cv.filter2D(frame, -1, filter)
    res[200:300, 200:300] = point
    detect = res[200:300, 200:300]

    if  0 < np.average(detect) <= 85:
        cv.putText(res, "BLACK", (25, 50), font, fontSize, textColor, thickness)
    elif 85 < np.average(detect) <= 125:
        cv.putText(res, "GRAY", (25, 50), font, fontSize, textColor, thickness)
    else:
        cv.putText(res, "WHITE", (25, 50), font, fontSize, textColor, thickness) 


    cv.imshow("frame", res)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()