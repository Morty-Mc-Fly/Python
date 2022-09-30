def inputnum():
    try:
        return int(input("Number : "))
    except ValueError:
        print("Invalid input")
        return inputnum()


def end():
    arr = []
    while True:
        inp = inputnum()
        if inp == 0:
            print("Input canceled")
            return arr
        else:
            arr.append(inp)


print(end())
