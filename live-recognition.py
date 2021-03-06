import numpy as np
import tensorflow as tf
import cv2
import pygame

cap = cv2.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 600)

music_file = 'music/song.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(music_file)
volume = 0.1
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()

IMG_CLASS_DICT = {
    0:'down',
    1:'none',
    2:'start',
    3:'stop',
    4:'up'
}

model = tf.keras.models.load_model('models/music-gesture-model.h5')

while(True):

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (398,98), (902,602), (255,255,255), 2)
    cv2.imshow('frame',frame)
  
    roi = frame[100:600, 400:900]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (250, 250))

    pred = model.predict(np.array([img]))
    pred_num = np.argmax(pred, axis=1)
    pred_num = pred_num[0]

    if(pred_num == 0):
        if(volume > 0):
            volume = volume - 0.1
        pygame.mixer.music.set_volume(volume)
        print('vol down')
    elif(pred_num == 2):
        pygame.mixer.music.unpause()
        print('start')
    elif(pred_num == 3):
        pygame.mixer.music.pause()
        print('stop')
    elif(pred_num == 4):
        if(volume < 1):
            volume = volume + 0.1
        pygame.mixer.music.set_volume(volume)
        print('vol up')

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    


