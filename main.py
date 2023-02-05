import time
import numpy as np
from mss import mss
import pyautogui as pg
import keyboard
from win32api import GetSystemMetrics
global monitor
print('Working')
monitor={}

def Mons():
    Mon = str(GetSystemMetrics(0)) + 'x' + str(GetSystemMetrics(1))
    if Mon == "1920x1080":
        monitors = {
            "left": 361,
            "top": 585,
            "width": 9,
            "height": 59,
        }
        monitor.update(monitors)

    elif Mon == "1280x720":
        monitors = {
            "left": 247,
            "top": 425,
            "width": 9,
            "height": 59,
        }
        monitor.update(monitors)
    elif Mon == "1366x768":
        monitors = {
            "left": 262,
            "top": 462,
            "width": 9,
            "height": 59,
        }
        monitor.update(monitors)
    elif Mon == "1440x900":
        monitors = {
            "left": 274,
            "top": 507,
            "width": 9,
            "height": 59,
        }
        monitor.update(monitors)
    else:
        print('Ваше разрешение экрана не подходит')
# Set the color to search for
our_color = [255, 255, 255]
Mons()
# Function to find the color on the screen
def find_color(our_color, monitor={}):
    #Поиск цвета на экране
    #Возьмем кусок экрана
    m = mss()
    # Получаем пиксель с экрана монитора
    img = m.grab(monitor)

    # Преобразуем этот пиксель в матрицу
    img_arr = np.array(img)

    #поиск цвета (b,g,r alpha)
    our_map = (our_color[2], our_color[1], our_color[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd
#255 255 255

# Main loop
while True:
    # Check if the user has pressed the "Esc" key
    if keyboard.is_pressed("esc"):
        print("Stop")
        # Wait for the user to press the "Enter" key to continue
        keyboard.wait("enter")
        print("Working")

    # Find the color on the screen
    result = find_color(our_color, monitor)

    # If the color was found, move the mouse cursor to that location
    if result.__len__():
        x = result[0][1] + monitor.get("left")
        y = result[0][0] + monitor.get("top")
        keyboard.send("ctrl")
