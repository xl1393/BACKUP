import numpy as np
import cv2
import h5py

def imhist(im):
  # calculates normalized histogram of an image
	m, n = im.shape
	h = [0.0] * 256
	for i in range(m):
		for j in range(n):
			h[im[i, j]]+=1
	return np.array(h)/(m*n)

def cumsum(h):
	# finds cumulative sum of a numpy array, list
	return [sum(h[:i+1]) for i in range(len(h))]

def histeq(im):
	#calculate Histogram
	#h = imhist(im)
    h = cv2.calcHist([im],[0],None,[256],[0,256])/(im.shape[0]*im.shape[1])
    h=h.reshape([256,])

    cdf = np.array(cumsum(h)) #cumulative distribution function
    sk = np.uint8(255 * cdf) #finding transfer function values
    s1, s2 = im.shape
    Y = np.zeros_like(im)
	# applying transfered values for each pixels
    for i in range(0, s1):
        for j in range(0, s2):
            Y[i, j] = sk[im[i, j]]
    H = imhist(Y)
	#return transformed image, original and new istogram, 
	# and transform function
    return Y , h, H, sk

#test PMD2501 data
#F70 bright,F71 dark  
#test 12bit to 16bit
#imgname='/sonas-hs/mitra/hpc/home/xli/MATdata/M919-F107--_3_0321.mat'
F70='/sonas-hs/mitra/hpc/home/xli/PMD2500/PMD2501&2500-F70-2016.03.03-19.03.40_PMD2500_3_0210_lossless.jp2'
F71='/sonas-hs/mitra/hpc/home/xli/PMD2500/PMD2501&2500-F71-2016.03.03-19.27.02_PMD2500_1_0211_lossless.jp2'
#data=h5py.File(imgname)
#img=np.asarray(data['img']
#img=img.T

img=cv2.imread(F71,-1)
img8=img.astype('uint8')
#cv2.imwrite('F71-8.jp2',img8)

#normalization1: bgr2yuv,eq,yuv2bvgr
#img_yuv=cv2.cvtColor(img8,cv2.COLOR_BGR2YUV)
#img_yuv[:,:,0]=cv2.equalizeHist(img_yuv[:,:,0])
#img_output=cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)
#cv2.imwrite('F71-8-yuv.jp2',img_output)

#normalization2: individual color channel
def Perchannel_equalizeHist(img):
    for c in xrange(0,2):
        img[:,:,c]=cv2.equalizeHist(img[:,:,c])
    return img

#img8Gray=cv2.cvtColor(img8,cv2.COLOR_BGR2GRAY)
img_1=cv2.cvtColor(img8,cv2.COLOR_BGR2YCR_CB)
img_1[:,:,0],h,newh,sk=histeq(img_1[:,:,0])
#eq,h,newh,sk=histeq(img8Gray)
img_2=cv2.cvtColor(img_1,cv2.COLOR_YCR_CB2BGR)
cv2.imwrite('F71-8-ycrcb-eq.jp2',img_2)
#img_output=Perchannel_equalizeHist(img8)
#cv2.imwrite('F70-8-gray.jp2',img8Gray)



#test histogram later



