import time

def inactive_state():
    while True:
        print("I ain active rn")
        time.sleep(2)
        # allot of code yes
        x = input("should i activate y/n")
        time.sleep(2)
        if x == "y":
            break