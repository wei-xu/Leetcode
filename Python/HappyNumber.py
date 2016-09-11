def isHappy(n):
    loop_detect = set()
    while n != 1:
        if n not in loop_detect:
            loop_detect.add(n)
        else:
            return False
        tmp = 0
        num_string = str(n)
        for i in num_string:
            tmp += int(i) ** 2
        n = tmp
    return True

# print isHappy(1)
# print isHappy(2)
# print isHappy(3)
print isHappy(11)