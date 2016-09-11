def isUgly(num):
    print num,
    if num == 1:
        return True
    if num <= 0:
        return False
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
        elif num % 5 == 0:
            num = num / 5
        else:
            return False
    return True

print isUgly(1)
print isUgly(2)
print isUgly(3)
print isUgly(4)
print isUgly(5)
print isUgly(6)
print isUgly(8)
print isUgly(14)
print isUgly(17)