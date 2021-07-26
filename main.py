def basic(a, z):
    b = 0
    while a != 1:
        if z:
            print(int(a))
        if a % 2 == 0:
            a /= 2

        else:
            a = 3 * a + 1
        b += 1
    return int(b)


def findmax(a):
    b = 1
    temp = 0
    while b < (a + 1):
        temp2 = basic(b, False)
        if temp2 > temp:
            temp = temp2
            tempnum = b
        b += 1
    basic(tempnum, True)
    return temp


print(basic(100,False))
