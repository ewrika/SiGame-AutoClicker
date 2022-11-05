import  time
import numpy as np
from mss import mss
import pyautogui as pg
import keyboard

monitor = {
    "left": 361,
    "top": 585,
    "width": 9,
    "height": 59,
}
def find_color(our_color,monitor={}):
    #Поиск цвета на экране
    #Возьмем кусок экрана
    m = mss()

    # Получаем пиксель с экрана монитора
    img = m.grab(monitor)
    # Преобразуем этот пиксель в матрицу
    img_arr =np.array(img)
    #поиск цвета (b,g,r alpha)
    our_map = (our_color[2],our_color[1],our_color[0],255)
    indexes = np.where(np.all(img_arr==our_map,axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd

#255 255 255

our_color = [255,255,255]


while True:
    time1= time.time()
    result = find_color(our_color,monitor)
    time2=time.time()
    if result.__len__():
        x = result[0][1]+ monitor.get('left')
        y = result[0][0] + monitor.get('top')
        print(time2-time1,[x,y])
        pg.moveTo(x,y) # Направляет на искомый цвет в диапазоне
        keyboard.send("ctrl")
