# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread("data/oden.png", cv2.IMREAD_COLOR)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('data/oden_write.png', img)

# plt.imshow(img[:,:,::-1], interpolation = "bicubic")
# plt.xticks([]), plt.yticks([])
# plt.show()


a = np.arange(27).reshape((3,3,3))
print(a)

print(a[:,:,::-1])
