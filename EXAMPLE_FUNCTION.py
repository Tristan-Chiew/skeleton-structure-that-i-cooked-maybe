import csv

def loadfile(filename):
    mylist = []
    with open(filename) as numbers:
        numbers_data = csv.DictReader(numbers, delimiter=',')
        for row in numbers_data:
            mylist.append(row)
    return mylist

drinks_list = loadfile('example.csv')
def drink_selector9000():
    while True:
        try:
            print("Input a number 0 - 9 to select a drink")
            print("Input # to exit")
            i = input("enter: ")
            if i == "#":
                print("exiting function")
                return 0
            else:
                x = int(i)
            if x < 0 or x >= len(drinks_list):
                print("Please enter a valid number between 0 and 9.")
                continue
            drink = drinks_list[x]
            print(f"You have selected {drink['name']}, it costs {drink['cost']} dollars")
            confirm = input("Do you confirm this choice? Press 0 for yes, any other key for no")
            if int(confirm) == 0:
                return drink
        except ValueError:
            print("Invalid input. Please enter a valid number.")

