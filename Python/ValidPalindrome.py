class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        # time limit exceed

        # while len(s) > 1:
        #     if not s[0].isalnum():
        #         s = s[1:]
        #         continue
        #     if not s[-1].isalnum():
        #         s = s[:-1]
        #         continue
        #     if s[0].lower() != s[-1].lower():
        #         return False
        #     s = s[1:-1]
        # return True

        # memory limit exceed

        # if s == "":
        #     return True
        # if len(s) == 1:
        #     return True
        # s = s.lower()
        # if not s[0].isalnum():
        #     return self.isPalindrome(s[1:])
        # if not s[-1].isalnum():
        #     return self.isPalindrome(s[:-1])
        # if s[0] == s[-1]:
        #     return self.isPalindrome(s[1:-1])
        # else:
        #     return False

s = Solution()
# print s.isPalindrome("A man, a plan, a canal: Panama")
# print s.isPalindrome("")
# print s.isPalindrome("race a car")
# print s.isPalindrome(" ")
# print s.isPalindrome("a,,.a")
# print s.isPalindrome("..a,,,")
# print s.isPalindrome("a.a.aba.,a.a")
print s.isPalindrome(".,")