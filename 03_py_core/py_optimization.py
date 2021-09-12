# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

e1 = cv.getTickCount()
e2 = cv.getTickCount()
time = (e2-e1) / cv.getTickFrequency()
print(time)


img1 = cv.imread("data/oden.png")
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2-e1)/cv.getTickFrequency()
print(t)

print(cv.useOptimized())
