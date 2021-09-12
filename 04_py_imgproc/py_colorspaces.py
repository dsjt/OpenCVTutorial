# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(*flags, sep="\n")

cap = cv.VideoCapture("data/sample.mp4")

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([0, 0, 0])
    upper_blue = np.array([90, 100, 100])

    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
