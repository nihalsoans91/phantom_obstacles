import numpy as np
import cv2
import time

class rem_noise:
    def __init__(self):
        self.image = cv2.imread("sample.jpg",0)
        self.w=self.image.shape[0]
        self.h=self.image.shape[1]
        self.k=41 # this is the kernel size
        self.k2=2 # this isthe inner kernel size
        self.start_time = time.time()
        self.filter_gap=int((self.k/2)-1)
        self.window_right=self.w-self.k
        self.window_down=self.h-self.k

    def save_frame(self,loc):
        cv2.imwrite(loc,self.image)

    def find_255(img):
        w = img.shape[0]
        h = img.shape[1]

        for r in range(w):
            for c in range(h):
                if img[r][c] == 255:
                    return True
                else:
                    continue

    def remove_phan_obj(self,img):
        self.image=np.copy(img)
        for d in range(self.window_down):
            for r in range(self.window_right):
                #det_filter=image[int(k*r):int(k*(r+1)),int(k*r):int(k*(r+1))]
                outer_filter=np.copy(self.image[d:d+self.k,r:r+self.k]) #ymin,ymax
                inner_filter=np.copy(outer_filter[self.filter_gap:self.filter_gap+self.k2,self.filter_gap:self.filter_gap+self.k2])
                if np.max(inner_filter) == 255:
                    outer_filter[self.filter_gap:self.filter_gap+self.k2,self.filter_gap:self.filter_gap+self.k2]=0
                    if np.max(outer_filter) == 255:
                    #if find_255(outer_filter):
                        continue
                    else:
                        self.image[d:d+self.k,r:r+self.k]=outer_filter
                        #cv2.imwrite("right\conv"+str(r)+str(d)+".jpg",image)
                else:
                    continue
        return(self.image)