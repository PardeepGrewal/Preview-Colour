import cv2 as cv
import numpy as np

cv.namedWindow("Preview Colour")

def dummy(dum):
    pass

cv.createTrackbar("Red", "Preview Colour",0, 255, dummy)
cv.createTrackbar("Green", "Preview Colour",0, 255, dummy)
cv.createTrackbar("Blue", "Preview Colour",0, 255, dummy)

img = np.zeros((250,600,3), np.uint8)

while(1):
    cv.imshow('Preview Colour', img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
    r = cv.getTrackbarPos('Red','Preview Colour')
    g = cv.getTrackbarPos('Green', 'Preview Colour')
    b = cv.getTrackbarPos('Blue', 'Preview Colour')
    
    img[:] = [b,g,r]

cv.destroyAllWindows()
