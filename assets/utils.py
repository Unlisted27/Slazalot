#General functions
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

menu(["One","Two","Thirty-five"])