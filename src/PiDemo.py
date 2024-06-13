# System imports
import socket
import time
from time import sleep


# Local imports

#from ..hal import hal_dc_motor as dc_motor


from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
from hal import hal_keypad as keypad
from hal import hal_rfid_reader as rfid
from hal import hal_ir_sensor as ir_sensor
import version as ver


while True:


def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def rotate_servo():
    servo.init()

    for i in range(0, 180, 5):
        servo.set_servo_position(i)
        sleep(0.05)


def test_motor():
    dc_motor.init()
    dc_motor.set_motor_speed(100)

    sleep(2)

    dc_motor.set_motor_speed(0)

def main():
    # Instantiate and initialize the LCD driver
    lcd = LCD.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    lcd.lcd_clear()
    lcd.lcd_display_string("DevOps for AIoT", 1)  # write on line 1
    lcd.lcd_display_string("Rel = " + ver.rel_ver, 2)  # write on line 2
    # starting on 3rd column

    sleep(2)  # wait 2 sec

    # Get IP address
    local_ip_address = socket.gethostbyname("raspberrypi")

    # Buzzer beep
    buzzer.init()
    buzzer.beep(0.5, 0.5, 4)

    blink_led(1)

    rotate_servo()

    test_motor()


# Main entry point
if __name__ == "__main__":
    main()
