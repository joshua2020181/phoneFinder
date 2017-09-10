import cv2
import numpy as np
import os
from tqdm import tqdm
from random import shuffle

TRAIN_DIR = 'C:/Users/joshc/Desktop/Python/Robot/images'

def classifyImage(img):
    name = img.split('.')[-3]
    if name == 'nothing':
        return [1,0,0]
    elif name == 'phone':
        return [0,1,0]
    elif name == 'keys':
        return [0,0,1]
    

def resizeImage():
    trainingData = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = classifyImage(img)
        #print(img)
        path = os.path.join(TRAIN_DIR,img)
        #print(path)
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        #img = cv2.imread('C:/Users/joshc/Desktop/Python/Robot/image.jpg' ,cv2.IMREAD_GRAYSCALE)
        #cv2.imshow('img',img)
##        k = cv2.waitKey(30) & 0xff
##        if k == 27:
##            break
        img = cv2.resize(img, (150,100))
        trainingData.append([np.array(img), np.array(label)])
    cv2.destroyAllWindows()
    shuffle(trainingData)
    np.save('trainingData.npy',trainingData)
    print('done')
    return trainingData

resizeImage()
