import csv
import time_out

def loadfile(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.DictReader(numbers, delimiter=',')
        for row in numbers_data:
            mylist.append(row)
    return mylist

drinks_list = loadfile('example.csv')

def drink_selector9000():
    while not time_out.check_timeout():
        try:
            print("Input a number 0 - 9 to select a drink")
            print("Input # to exit")
            i = time_out.input_with_timeout("enter: ", 30)
            if i == "#":
                print("exiting function")
                return 0
            elif int(i) == -1:
                break
            else:
                x = int(i)
            if x < 0 or x >= len(drinks_list):
                print("Please enter a valid number between 0 and 9.")
                continue
            drink = drinks_list[x]
            print(f"You have selected {drink['name']}, it costs {drink['cost']} dollars")
            confirm = time_out.input_with_timeout("Do you confirm this choice? Press 0 for yes, any other key for no", 30)
            if int(confirm) == 0:
                return drink
            elif int(confirm) == -1:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

