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
start_pos = 0
stop_pos = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    stop_pos = stop_pos + 1
    #print(cap.get(cv2.CAP_PROP_POS_MSEC))
    if check_start == 0:
        foto = frame[0][0]
        print("Кадр для сравнения")
        print(foto)
        check_start = 1
    try:
        cv2.imshow('frame', frame)
    except Exception as e:
        stop_pos_sec = round(fix_pos / 27)
        ffmpeg_extract_subclip('C:\\Users\\Admin\\Videos\\Юра3.mp4', start_pos, stop_pos_sec,
                               f'C:\\Users\\Admin\\Videos\\Юра3_{start_pos}.mp4')
        print(f"Нарезка последнего фрагмента прошла успшно Старт:{start_pos} Финиш:{stop_pos_sec}  Ошибка:{e}")
        break
    if foto[0] == frame[0][0][0]:
        fix_pos=round(stop_pos / 27)
        print(f"Обнаруженно совпадение {round(stop_pos / 27)}")
        spam = 0
        count_cadres = count_cadres + 1
    else:
        spam = spam + 1
        if spam > 1080:
            if count_cadres > 19:
                print(f"Кадр для сравнения попался {count_cadres} раз подряд. Сейчас будет нарезка")
                print(frame[0][0])
                stop_pos_sec = round(fix_pos / 27)
                print(f"{stop_pos_sec} == {start_pos}")
                if (stop_pos_sec - start_pos) > 10:
                    ffmpeg_extract_subclip('C:\\Users\\Admin\\Videos\\Юра3.mp4', start_pos, stop_pos_sec,
                                           f'C:\\Users\\Admin\\Videos\\Юра3_{start_pos}.mp4')
                    print(f"Нарезка прошла успшно Старт:{start_pos} Финиш:{stop_pos_sec}")
                    start_pos = stop_pos_sec
                else:
                    start_pos = stop_pos_sec
                    print("Видео для нарзеки оказалось слишком коротким")
            count_cadres = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # print(round(stop_pos / 60))

cap.release()
cv2.destroyAllWindows()
