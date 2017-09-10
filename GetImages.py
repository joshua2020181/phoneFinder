import cv2
import time

STARTNUMBER = 0

camera_port = 0

ramp_frames = 30 #number of frames to throw away
 
camera = cv2.VideoCapture(camera_port)

obj = 'nothing' #nothing, phone, keys

for i in range(3):
    print(i)
    time.sleep(1)

def get_image():
    retval, im = camera.read()
    return im

for i in range(ramp_frames):
 temp = get_image()

for x in range(1000):
    print("Taking image " + str(x))

    camera_capture = get_image()
    cv2.imshow('camera', camera_capture)
    y = x
    y += STARTNUMBER
    y = str(y)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    path = "C:/Users/joshc/Desktop/Python/Robot/images/"
    name = obj + '.' + y + '.jpg'
    name = path + name
    cv2.imwrite(name, camera_capture)
    time.sleep(0.1)
del(camera)
