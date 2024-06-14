import threading

timeout_occurred = False

def input_with_timeout(prompt, timeout):
    global timeout_occurred
    def timer_func():
        global timeout_occurred
        timeout_occurred = True
        print("timeout occurred")
        return -1

    # Start the timer thread
    timer = threading.Timer(timeout, timer_func)
    timer.start()

    try:
        # Input prompt
        user_input = input(prompt)
    except:
        pass
    finally:
        # Cancel the timer if input is received
        timer.cancel()

    return user_input

def check_timeout():
    return timeout_occurred
