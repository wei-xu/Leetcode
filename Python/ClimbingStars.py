'''
Fibonacci and dynamic programming
'''
def climbStars(n):
    if n == 1 or n == 2:
        return n
    f1 = 1
    f2 = 2
    fn = 0
    for i in range(3, n + 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn


print climbStars(1)
print climbStars(2)
print climbStars(3)
print climbStars(4)