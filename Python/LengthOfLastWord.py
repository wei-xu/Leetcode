class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.strip().split(' ')
        return len(s_list[-1])