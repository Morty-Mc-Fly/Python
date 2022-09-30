
def end():
    arr = []
    while True:
        inp = input("\tEingabe : ")
        if inp == "Beenden":
            print("Input canceled")
            return arr
        else:
            arr.append(inp)


print(end())
