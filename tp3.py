import cv2
import numpy as np

img = cv2.imread("un.jpg", cv2.IMREAD_GRAYSCALE)

vois = 3
def filreMoy(img):
    h,w = img.shape
    imgMoy = np.zeros(img.shape, img.dtype)
    for y in range(h):
        for x in range(w):
            if (y<vois/2) or y>(h-vois/2) or (x<vois/2) or x>(w-vois/2):
                imgMoy[y,x] = img[y,x]
            else:
                imgVois = img[int(y-vois/2):int(y+vois/2),int(x-vois/2):int(x+vois/2)]
                moy =0
                for yv in range(imgVois.shape[0]):
                    for xv in range(imgVois.shape[1]):
                        moy += imgVois[yv, xv]
                imgMoy[y,x] = int(moy/(vois*vois))
    return imgMoy
imgMoy = filreMoy(img)                


def filreMediane(img):
    h,w = img.shape
    imgMed = np.zeros(img.shape, img.dtype)
    for y in range(h):
        for x in range(w):
            if (y<vois/2) or y>(h-vois/2) or (x<vois/2) or x>(w-vois/2):
                imgMed[y,x] = img[y,x]
            else:
                imgVois = img[int(y-vois/2):int(y+vois/2),int(x-vois/2):int(x+vois/2)]
                t = np.zeros((vois*vois), np.uint8)
                for yv in range(imgVois.shape[0]):
                    for xv in range(imgVois.shape[1]):
                        t[yv*vois+xv] = imgVois[yv,xv]
                        
                t.sort()
                imgMed[y,x] = t[int((vois*vois-1)/2)]
                imgMed[y,x] = np.median(imgVois)
                #imgMed[y,x] = np.mean(imgVois)
          
    return imgMed
imgMed = filreMediane(img)

cv2.imshow("image avant", img)
cv2.imshow("image apres Moy", imgMoy)
cv2.imshow("image apres Med", imgMed)
cv2.waitKey(0)
cv2.destroyAllWindows() 