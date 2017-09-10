import numpy as np
from alexnet import alexnet2
import cv2
import time
import os
from tqdm import tqdm
from random import shuffle

camera_port = 0

ramp_frames = 30 #number of frames to throw away
 
camera = cv2.VideoCapture(camera_port)

WIDTH = 150
HEIGHT = 100
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'model-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)
DIR = 'C:/Users/joshc/Desktop/Python/Robot/testImages'

model = alexnet2(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
 temp = get_image()

def main():
    img = get_image()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (WIDTH,HEIGHT))
    prediction = TestModel(img)
    prediction = str(prediction)
    prediction = list(prediction)
    answer = []
    b = 0
    for a in range(len(prediction)):
        if prediction[a] == '.':
            answer.append(prediction[a+1])
    print(answer)
    print(answer.index(max(answer)))
    if answer.index(max(answer)) == 0:
        print('nothing')
    elif answer.index(max(answer)) == 1:
        print('phone')
    elif answer.index(max(answer)) == 2:
        print('keys')
    time.sleep(1)

##cv2.waitKey(0)
##cv2.destroyAllWindows()

def TestModel(img):
    
    prediction = model.predict([img.reshape(WIDTH,HEIGHT,1)])[0]
    print(prediction)
    return(prediction)

##for i in range(10):
##    x = i+1
##    fileName = DIR + '/' + str(x) + '.jpg'
##    img = cv2.imread(fileName,0)
##    img = cv2.resize(img, (WIDTH,HEIGHT))
##    main()

while True:
    main()
