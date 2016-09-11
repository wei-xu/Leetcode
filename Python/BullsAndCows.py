from collections import Counter
class Solution(object):
    def getHintShort(self, secret, guess):
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        tracking = dict()
        num_bulls = 0
        num_cows = 0
        guess_revised = ""
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_bulls += 1
            else:
                guess_revised += guess[i]
                if secret[i] not in tracking:
                    tracking[secret[i]] = 1
                else:
                    tracking[secret[i]] += 1
        for i in range(len(guess_revised)):
            if guess_revised[i] in tracking:
                num_cows += 1
                tracking[guess_revised[i]] -= 1
                if tracking[guess_revised[i]] == 0:
                    del tracking[guess_revised[i]]
        return "%dA%dB" % (num_bulls, num_cows)

s = Solution()
# print s.getHint("1807", "7810")
# print s.getHint("1123", "0111")
# print s.getHint("0123", "0123")
# print s.getHint("0123", "0312")
# print s.getHint("0011", "2345")
print s.getHint("0011", "1100")
print s.getHintShort('1102', '1103')
print s.getHint('1102', '1103')