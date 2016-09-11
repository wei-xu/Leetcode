class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        last_term = "11"
        for _ in range(2, n):
            new_term = ""
            counter = 1
            l = len(last_term)
            last_term = last_term + "q"
            for i in range(0, l):
                if last_term[i] == last_term[i + 1]:
                    counter += 1
                else:
                    new_term += str(counter) + last_term[i]
                    counter = 1
            if new_term == "":
                new_term += str(counter) + last_term[0]
            last_term = new_term
        return last_term

s = Solution()
# print s.countAndSay(1)
# print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
print s.countAndSay(6)
print s.countAndSay(7)