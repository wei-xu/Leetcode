# def hammingWeight(n):
#     obj = bin(n)[2:]
#     output = 0
#     for i in obj:
#         if i == '1':
#             output += 1
#     return output

def hammingWeight(n):
    if n == 0 or n == 1:
        return n
    c = 0
    while(n != 1):
        if n % 2 == 1:
            c += 1
        n = n / 2
    return c + 1

print hammingWeight(16)
print hammingWeight(0)
print hammingWeight(1)
print hammingWeight(11)
print hammingWeight(15)