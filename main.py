import time
import numpy as np
from mss import mss
import pyautogui as pg
import keyboard

# Set up the monitor region to search
monitor = {
    "left": 361,
    "top": 585,
    "width": 9,
    "height": 59,
}

# Set the color to search for
our_color = [255, 255, 255]

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
        pg.moveTo(x, y)  # Move to the found color
        keyboard.send("ctrl")
