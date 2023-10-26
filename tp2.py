import cv2
import numpy as np

img = cv2.imread("7_2.jpg", cv2.IMREAD_GRAYSCALE)

#ce code psq j'ai pas une image super a 255
#img[:] = img[:]/2
#cv2.imwrite("7_2.jpg",img) #sauvegarder

if img is None:
    print("Erreur de chargement")
    exit(0)

h,w = img.shape
min, max = 255, 0
for y in range(h):
    for x in range(w):
        if(img[y,x]>max):
            max = img[y,x]
        if(img[y,x]<min):
            min = img[y,x]    
print(min, max)
img_apres = np.zeros(img.shape, img.dtype)
for y in range(h):
    for x in range(w):
        img_apres[y,x] = (img[y,x]-min)*255/(max-min)

print("min: ",min," max: ",max)

cv2.imshow("image avant",img)  
cv2.imshow("image apres",img_apres)   

import matplotlib.pyplot as plt
#pour chaque niv deg on calcule le nbr de pix
hist_avant = np.zeros((256,1),np.uint16)  #nbr de pix
for y in range(h):
    for x in range(w):
        hist_avant[img[y,x]] +=1
hist_apres = cv2.calcHist([img_apres],[0],None,[256],[0,255]) #une fct predifinie = le code avant

plt.figure()
plt.title("image normalisee")
plt.xlabel("NG")
plt.ylabel("NG_Pixeles")
plt.plot(hist_avant)
plt.plot(hist_apres)
plt.xlim([0,255])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()  