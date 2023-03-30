import cv2
from cvzone.PoseModule import PoseDetector
import cvzone
import time
import numpy as np

cap= cv2.VideoCapture(0)  #we make a variable of cap nd save Videocapture

detector = PoseDetector()
ptime = 0
ctime= 0
color = (0,0,255)
dir = 0 #direction
pushup  = 0
while True:
    _,  img = cap.read() #captured video read and store in img
    img = detector.findPose(img, )
    lmlst, bbox=detector.findPosition(img, draw = False)
    if lmlst:
        #print(lmlst)
        a1= detector.findAngle(img,27,25,23)
        a2 = detector.findAngle(img, 28,24,26)
        per_val1 = np.interp(a1,(80,175),(100,0))
        #print(per_val1)
        per_val2 = np.interp(a1, (80, 175), (100, 0))
        #print(per_val2)
        bar_val1 = int(np.interp(per_val1, (0, 100), (40 + 350, 40)))
        bar_val2 = int(np.interp(per_val2, (0, 100), (40 + 350, 40)))
        #bar1
        cv2.rectangle(img, (570, bar_val1), (570 + 35, 40 + 350),color, cv2.FILLED)
        cv2.rectangle(img,(570,40), (570+35,40+350),(),3)

        #bar 2
        cv2.rectangle(img, (60, bar_val2), (60 + 35 , 40 + 350),color, cv2.FILLED)
        cv2.rectangle(img, (60, 40), (60 + 35, 40 + 350), (), 3)
        #bar 2 percentage
        cvzone.putTextRect(img,f'{per_val2}%',(25,25),1.1,2,colorT=(255,255,255),colorR=color,border=3,colorB=())

        #bar 1 percenatage
        cvzone.putTextRect(img, f'{per_val1}%', (570, 25), 1, 2, colorT=(255, 255, 255), colorR=color, border=3,
                           colorB=())

        # print(per_val1)
        #bar_val2 = np.interp(a1, (75, 175), (100, 0))
        if per_val1 and per_val2 == 100:
            if dir== 0:
                pushup  +=0.5
                dir =1
                color= (0,255,0)
        elif per_val1 == 0 and per_val2 == 0:
            if dir ==1:
                pushup += 0.5
                dir = 0
                color = (0,255,0)
        else:
            color = (0,0,255)
        #print(pushup)
        cvzone.putTextRect(img,f'pushups:{int(pushup)}', (290,35),2, 2, colorT=(255, 255, 255), colorR=(255,0,0), border=3,
                           colorB=())

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime= ctime
    cvzone.putTextRect(img,f'FPS: (int{fps})',(288,440),0.9,2,colorT=(255,255,255),colorR=(0,155,0),border=3,colorB=())
    cv2.imshow("Pushup counter",img)
    if cv2.waitKey(1) == ord("b"):
        break

cv2.destroyAllWindow()