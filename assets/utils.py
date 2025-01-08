#General functions
import os
def menu(options:list):
    length = 1
    i=1
    items = []
    for item in options:
        if type(item) != str:
            raise TypeError("Items in list must be type str")
        else:
            items.append(f"|[{i}]{item}")
            i+=1
    for thing in items:
        if len(thing) > length:
            length = len(thing)
    print("_"*length)
    for thing in items:
        print(thing)
    while True:
        try:
            answer = input("|:")
            selected = options[int(answer)-1]
            return(selected)
        except Exception as e:
            #print(e) #Uncomment this line to show error message when the user enters an invalid option
            print("Invalid selection, try again")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')