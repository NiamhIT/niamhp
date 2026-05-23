

import cv2
import time
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

x = int(input("How many times do you want the drone to fly?"))
y = int(input("How many photos do you want the drone to take?"))
z = int(input("How long do you want the drone to pause between taking photos?"))
e=  int(input("How far away is the target in cm?"))

flight = 0

while flight < x:

    tello.takeoff()
    tello.move_forward(e)
    pic = 0

    while pic < y:

        frame = frame_read.frame
        cv2.imwrite(f"flight{flight}_pic{pic}.png", frame)

        time.sleep(z)

        pic= pic+1

    tello.move_back(e)
    tello.land()

    flight=flight+1

tello.streamoff()
