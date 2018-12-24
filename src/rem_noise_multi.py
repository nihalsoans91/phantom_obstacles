import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import threading


def find_255(img):
    w = img.shape[0]
    h = img.shape[1]

    for r in range(w):
        for c in range(h):
            if img[r][c] == 255:
                return True
            else:
                continue


def right_filters(d):
    for r in range(window_right):
        # print(r)
        # det_filter=image[int(k*r):int(k*(r+1)),int(k*r):int(k*(r+1))]
        outer_filter = np.copy(image[d:d + k, r:r + k])  # ymin,ymax
        inner_filter = np.copy(outer_filter[filter_gap:filter_gap + k2, filter_gap:filter_gap + k2])
        if np.max(inner_filter) == 255:
            outer_filter[filter_gap:filter_gap + k2, filter_gap:filter_gap + k2] = 0
            if np.max(outer_filter) == 255:
                # if find_255(outer_filter):
                continue
            else:
                image[d:d + k, r:r + k] = outer_filter
                #cv2.imwrite("right\conv" + str(r) + str(d) + ".jpg", image)
        else:
            continue


image = cv2.imread("sample.jpg", 0)
# we have to ignore 0 and 127 the only issue is from 255
image[image < 255] = 0

w = image.shape[0]
h = image.shape[1]
print(w)
print(h)
image = cv2.imread("sample.jpg", 0)
k = 16  # this is the kernel size
k2 = 2  # this isthe inner kernel size
start_time = time.time()
filter_gap = int((k / 2) - 1)
window_right = w - k
window_down = h - k
d_m = 0
while d_m < window_down:
    d_m += 1
    try:
        th_1 = threading.Thread(target=right_filters, args=(d_m,))
        d_m += 1
        th_2 = threading.Thread(target=right_filters, args=(d_m,))
        d_m += 1
        th_3 = threading.Thread(target=right_filters, args=(d_m,))
        # th_1=_thread.start_new_thread ( right_filters, (d_m,) )
        # d_m+=1
        # th_2 = _thread.start_new_thread(right_filters, (d_m,))
        th_1.start()
        th_2.start()
        th_3.start()
        th_1.join()
        th_2.join()
        th_3.join()



    except Exception as ex:
        print(ex)

cv2.imwrite("postproc.jpg", image)

print("--- %s seconds ---" % (time.time() - start_time))
