import matplotlib.pyplot as plt
import numpy as np
import cv2
import time

def find_255(img):
    w = img.shape[0]
    h = img.shape[1]

    for r in range(w):
        for c in range(h):
            if img[r][c] == 255:
                return True
            else:
                continue


image = cv2.imread("sample.jpg",0)
# we have to ignore 0 and 127 the only issue is from 255


w=image.shape[0]
h=image.shape[1]
print(w)
print(h)
image = cv2.imread("sample.jpg",0)
k=16 # this is the kernel size
k2=2 # this isthe inner kernel size
start_time = time.time()
filter_gap=int((k/2)-1)
window_right=w-k
window_down=h-k
for d in range(window_down):
    for r in range(window_right):
        #det_filter=image[int(k*r):int(k*(r+1)),int(k*r):int(k*(r+1))]
        outer_filter=np.copy(image[d:d+k,r:r+k]) #ymin,ymax
        inner_filter=np.copy(outer_filter[filter_gap:filter_gap+k2,filter_gap:filter_gap+k2])
        if np.max(inner_filter) == 255:
            outer_filter[filter_gap:filter_gap+k2,filter_gap:filter_gap+k2]=0
            if np.max(outer_filter) == 255:
            #if find_255(outer_filter):
                continue
            else:
                image[d:d+k,r:r+k]=outer_filter
                #cv2.imwrite("right\conv"+str(r)+str(d)+".jpg",image)
        else:
            continue
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imwrite("postproc.jpg",image)