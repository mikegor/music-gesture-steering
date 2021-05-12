import cv2
import sys
import os
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 600)

IMG_FOLDER_PATH = r'C:\Users\mikeg\dev\MachineLearning\music-gesture-steering\image_data'

IMG_CLASS_DICT = {
    0:'up',
    1:'right',
    2:'down',
    3:'left',
    4:'none'
}

print('insert wanted class: 0:up, 1:right, 2:down, 3:left, 4:none')
num = int(input())
print('press s to start')
start = False
count = -1
while(True):
    if(count == 300):
        break
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (398,98), (902,602), (255,255,255), 2)
    cv2.imshow('frame',frame)
  
    if(start):
        roi = frame[100:600, 400:900]
        save_path = os.path.join(IMG_FOLDER_PATH, IMG_CLASS_DICT[num], '{}.jpg'.format(count+1))
        print(save_path)
        cv2.imwrite(save_path, roi)

    if(count == -1):
        k = cv2.waitKey(10)
        if k == ord('s'):
            start = True
        else:
            count=-2

    count = count+1

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    


