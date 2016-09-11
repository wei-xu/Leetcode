class Solution(object):
    def isStrobogrammaticShort(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = 0
        r = len(num) - 1
        while l <= r:
            if (num[l] == '6' and num[r] == '9') or (num[l] == '9' and num[r] == '6'):
                l += 1
                r -= 1
                continue
            if num[l] != num[r]:
                return False
            else:
                if num[l] != '1' and num[l] != '8' and num[l] != '0':
                    return False
            l += 1
            r -= 1
        # if l == r and not (num[l] == '1' or num[l] == '8' or num[l] == '0'):
        #     return False
        return True

s = Solution()
print s.isStrobogrammatic('818')
print s.isStrobogrammatic('69')
print s.isStrobogrammatic('88')
print s.isStrobogrammatic('81')
print s.isStrobogrammatic('2')
print s.isStrobogrammatic('8')
print s.isStrobogrammatic('84')
print s.isStrobogrammatic('838')
print s.isStrobogrammatic('33')