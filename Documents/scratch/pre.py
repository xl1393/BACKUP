import cv2
import numpy as np

img=cv2.imread('LossyTest.jp2')
'''
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

clahe=cv2.createCLAHE(clipLimit=10.0,tileGridSize=(10,10))
img_post=clahe.apply(img_gray)

img_result=cv2.cvtColor(img_post,cv2.COLOR_GRAY2BGR)

cv2.imwrite('clahe_lossytest.jp2',img_result)
'''
hsv=cv2.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
v+=255*5
final_hsv=cv2.merge((h,s,v))
img2=cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
cv2.imwrite('hsv_lossytest.jp2',img2)
