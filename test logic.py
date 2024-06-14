import threading
import sys

def display_ascii_art():
    ascii_art = """
      ____  _                    _     _ 
     |  _ \| | __ _ _   _  ___  | |__ (_)
     | | | | |/ _` | | | |/ _ \ | '_ \| |
     | |_| | | (_| | |_| |  __/ | | | | |
     |____/|_|\__,_|\__, |\___| |_| |_|_|
                    |___/                
    """
    print(ascii_art)

def input_with_timeout(prompt, timeout):
    def timer_func():
        display_ascii_art()
        return

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

if __name__ == "__main__":
    # Prompt the user with a 15-second timeout
    result = input_with_timeout("Please enter something within 15 seconds: ", 15)
    if result:
        print(f"You entered: {result}")
