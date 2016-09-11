def isPowerOfTwo(n):
    if n <= 0:
        return False
    if n & (n - 1) == 0:
        return True
    return False

print isPowerOfTwo(0)
print isPowerOfTwo(1)
print isPowerOfTwo(4)
print isPowerOfTwo(8)
print isPowerOfTwo(9)