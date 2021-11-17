""" Make a screen recorder in Python """

import cv2
import numpy as np
import pyautogui

#A display  screen resolution. get it from your OS settings
SCREEN_SIZE = (1920, 1080)

#Define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    #make a screenshot
    img =  pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break


cv2.destroyAllWindows()
out.release()

