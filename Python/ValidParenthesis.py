class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = list()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                lst.append(s[i])
            elif s[i] == '}':
                if len(lst) == 0 or lst.pop() != '{':
                    return False
            elif s[i] == ')':
                if len(lst) == 0 or lst.pop() != '(':
                    return False
            elif s[i] == ']':
                if len(lst) == 0 or lst.pop() != '[':
                    return False
            else:
                return False
        if len(lst) != 0:
            return False
        return True

s = Solution()
print s.isValid("()")