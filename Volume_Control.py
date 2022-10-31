import cv2 as cv
import time

import numpy as np

import Haand_detection_module as hdm
import math
import numpy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



a = cv.VideoCapture(0)
detector = hdm.HandDetector(detectionCon=0.7)
volPercentage = 0

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
VolRange = volume.GetVolumeRange()

minVol = VolRange[0]
maxVol = VolRange[1]
# vol = 0

def Volumecontrol():
    global volPercentage
    CTime = 0
    pTime = 0

    volBar = 400

    while True:
        success, img = a.read()
        img = detector.FindHands(img)



        lmlist = detector.FindPosition(img, draw=False )
        if len(lmlist) != 0:
            # print(lmlist[4], lmlist[8])


            x1, y1 = lmlist[4][1], lmlist[4][2]
            x2, y2 = lmlist[8][1], lmlist[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv.circle(img, (x1, y1), 10, (0, 0, 255), cv.FILLED )
            cv.circle(img, (x2, y2), 10, (0, 0, 255), cv.FILLED)
            cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv.circle(img, (cx, cy), 10, (0, 0, 255), cv.FILLED)
            length = math.hypot(x2 - x1, y2 - y1)
            # print(length)
            vol = np.interp(length, (50, 197), (minVol, maxVol))
            volBar = np.interp(length, (50, 197), (400, 150))
            volPercentage = np.interp(length, (50, 197), (0, 100))
            print(int(length), vol)
            if length < 50:
                cv.circle(img, (cx,cy), 10, (0, 255, 0), cv.FILLED)
            volume.SetMasterVolumeLevel(vol, None)

        cv.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)
        cv.putText(img, f'{int(volPercentage)}%', (40, 450), cv.FONT_ITALIC, 1, (0, 255, 0), 3)

        CTime = time.time()
        fps = 1 / (CTime - pTime)
        pTime = CTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_ITALIC, 2, (0, 255, 0), 3)

        cv.imshow('A_I', img)
        cv.waitKey(1)
if __name__ == "__main__":
    Volumecontrol()