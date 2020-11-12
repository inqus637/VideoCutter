import numpy as np
import cv2
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# ffmpeg_extract_subclip('D:\\Ковчег\\Идеи\\video(3).mkv',10,20,'D:\\Ковчег\\Идеи\\video(3)_cut.mkv')
foto = [[[]]]
cap = cv2.VideoCapture("D:\\Ковчег\\Идеи\\video(3).mkv")
count_cadres = 0
spam = 0
check_start = 0
stop_pos = 0
start_pos = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if check_start == 0:
        foto = frame[0][0]
        print("Кадр для сравнения")
        print(foto)
        check_start = 1
    cv2.imshow('frame', frame)
    # print("FRAME")
    if foto[0] == frame[0][0][0]:
        spam = 0
        count_cadres = count_cadres + 1
    else:
        spam = spam + 1
        if spam > 60:
            if count_cadres > 30:
                print(f"Кадр для сравнения попался {count_cadres} раз подряд. Сейчас будет нарезка")
                print(frame[0][0])
                print(f"{round(stop_pos / 60)} == {round(start_pos)}")
                if (round(stop_pos / 60) - round(start_pos)) > 5:
                    ffmpeg_extract_subclip('C:\\Users\\Admin\\Videos\\Юра3.mp4', round(start_pos), round(stop_pos / 60),
                                           f'C:\\Users\\Admin\\Videos\\Юра3_{count_cadres}.mp4')
                    print(f"Нарезка прошла успшно Старт:{round(start_pos)} Финиш:{round(stop_pos / 60)}")
                    start_pos = round(stop_pos / 60)
                else:
                    print("Видео для нарзеки оказалось слишком коротким")
            count_cadres = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    stop_pos = stop_pos + 1
    #print(round(stop_pos / 60))

cap.release()
cv2.destroyAllWindows()
