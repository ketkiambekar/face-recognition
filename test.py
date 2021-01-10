import cv2
import numpy as np
import os

imList =[]
os.chdir('/Users/ketkiambekar/Documents/Practice/Git/face-recognition/unknown_faces')
print(os.getcwd())

def image_grid(columns=5, images=[] ):
    rGrid = None
    i=0
    imStack=None
    for im in images:
        if i==0:
            i+=1
            imgStack=im
        else:
            imgStack = 
            i+=1
        if i==columns:
            if rGrid == None:
                rGrid=imgStack
            else:
                rGrid=np.vstack(rGrid, imgStack) 
            i=0
            imgStack=None

    return rGrid
   

for name in os.listdir():
    if not (str(name)).startswith('.'):
        img = cv2.imread(name)
        if img.all() != None:
            imList.append(img)
print(len(imList))
grid = image_grid(5, imList)
cv2.imshow("grid", grid)
 
