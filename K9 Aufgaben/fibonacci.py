def recursive(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index > 1:
        return recursive(index-1) + recursive(index-2)


print(recursive(10))
print(recursive(6))
print(recursive(3))
print(recursive(20))
print(recursive(30), "\n")


def iterative(index):
    firstadd = 0
    secadd = 1
    curr = 0

    for x in range(1, index):
        curr = firstadd + secadd
        firstadd = secadd
        secadd = curr
    return curr


print(iterative(20))
