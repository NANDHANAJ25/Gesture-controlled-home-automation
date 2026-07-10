import cv2
import mediapipe as mp
import serial
import time

ser = serial.Serial('COM3',115200)   # change COM port
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tipIds=[4,8,12,16,20]

while True:

    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    fingers=[]

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            lmList=[]

            for id,lm in enumerate(handLms.landmark):

                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmList.append((cx,cy))

            # Thumb
            if lmList[tipIds[0]][0] > lmList[tipIds[0]-1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for id in range(1,5):

                if lmList[tipIds[id]][1] < lmList[tipIds[id]-2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            data = ''.join(str(x) for x in fingers)

            ser.write((data+"\n").encode())

            mp_draw.draw_landmarks(img,handLms,mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control",img)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()