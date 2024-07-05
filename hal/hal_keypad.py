import RPi.GPIO as GPIO
from time import sleep, time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]  # layout of keys on keypad
ROW = [6, 20, 19, 13]  # row pins
COL = [12, 5, 16]  # column pins

global cbk_func
global key_pressed
global timeout_reached

def init(key_press_cbk):
    global cbk_func

    cbk_func = key_press_cbk

    # set column pins as outputs, and write default value of 1 to each
    for i in range(3):
        GPIO.setup(COL[i], GPIO.OUT)
        GPIO.output(COL[i], 1)

    # set row pins as inputs, with pull up
    for j in range(4):
        GPIO.setup(ROW[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_key():
    global cbk_func

    # scan keypad
    while True:
        for i in range(3):  # loop through all columns
            GPIO.output(COL[i], 0)  # pull one column pin low
            for j in range(4):  # check which row pin becomes low
                if GPIO.input(ROW[j]) == 0:  # if a key is pressed
                    cbk_func(MATRIX[j][i])
                    while GPIO.input(ROW[j]) == 0:  # debounce
                        sleep(0.1)
                    return  # exit the function after key press
            GPIO.output(COL[i], 1)  # write back default value of 1

        sleep(0.01)  # add a small delay to avoid excessive CPU usage

def timeout_thread(duration):
    global timeout_reached
    sleep(duration)
    timeout_reached = True

def get_key_timeout(timeout=20):
    global cbk_func, key_pressed, timeout_reached

    key_pressed = False
    timeout_reached = False

    # Start the timeout thread
    t = threading.Thread(target=timeout_thread, args=(timeout,))
    t.start()

    # scan keypad
    while not timeout_reached:
        for i in range(3):  # loop through all columns
            GPIO.output(COL[i], 0)  # pull one column pin low
            for j in range(4):  # check which row pin becomes low
                if GPIO.input(ROW[j]) == 0:  # if a key is pressed
                    cbk_func(MATRIX[j][i])
                    key_pressed = True
                    while GPIO.input(ROW[j]) == 0:  # debounce
                        sleep(0.1)
                    return  # exit the function after key press
            GPIO.output(COL[i], 1)  # write back default value of 1

        sleep(0.01)  # add a small delay to avoid excessive CPU usage

    if timeout_reached and not key_pressed:
        cbk_func(0)  # call the callback with 0 to indicate timeout
