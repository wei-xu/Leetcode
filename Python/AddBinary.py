class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a, 2)
        int_b = int(b, 2)
        return bin(int_a + int_b)[2:]

    def addBinaryR(self, a, b):
        pa = len(a) - 1
        pb = len(b) - 1
        carry = 0
        output = ""
        while pa >= 0 and pb >= 0:
            int_pa = int(a[pa])
            int_pb = int(b[pb])
            ans = int_pa + int_pb + carry
            carry = ans / 2
            output += str(ans % 2)
            pa -= 1
            pb -= 1
        while pa >= 0:
            int_pa = int(a[pa])
            ans = int_pa + carry
            carry = ans / 2
            output += str(ans % 2)
            pa -= 1
        while pb >= 0:
            int_pb = int(b[pb])
            ans = int_pb + carry
            carry = ans / 2
            output += str(ans % 2)
            pb -= 1
        if carry != 0:
            output += '1'
        return output[::-1]

s = Solution()
print s.addBinaryR('100', '1')