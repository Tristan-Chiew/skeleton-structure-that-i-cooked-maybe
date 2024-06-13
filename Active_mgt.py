


import EXAMPLE_FUNCTION
import time
import example_payment




def active_state():
    while True:
        print("im active ok")
        time.sleep(2)
        drink_chosen = EXAMPLE_FUNCTION.drink_selector9000()
        time.sleep(2)
        if drink_chosen == 0:
            x = input("Sleepy time? y/n")
            time.sleep(2)
            if x == "y":
                break
        else:
            example_payment.payment(drink_chosen)
            x = input("Sleepy time? y/n")
            time.sleep(2)
            if x == "y":
                break