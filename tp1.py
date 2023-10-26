import cv2
import numpy as np


#img2 = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("7_2.jpg", cv2.IMREAD_GRAYSCALE)
if img2 is None:
    print("Erreur de chargement")
    exit(0)

#image en couleur=> 3D (h,w,c)
#image niv degre=> 2D  (h,w)

h, w = img2.shape
print(h,w, img2[10, 10])

#img = np.zeros(img2.shape, np.uint8) 

imgResult = np.zeros(img2.shape, img2.dtype) 
#img[100:300, 100:300] = 128

print(img2.dtype)
#cv2.imshow("image1",imgResult)
#cv2.imshow("image2",img2)


for y in range(img2.shape[0]):
    for x in range(img2.shape[1]):
        imgResult[y,x] = 255- img2[y,x]




cv2.imshow("image1",imgResult)     
cv2.waitKey(0)
cv2.destroyAllWindows()   
