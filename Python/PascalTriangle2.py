class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lastList = [1,1]
        if rowIndex == 0:
            return [1]
        for i in range(2, rowIndex + 1):
            thisList = list()
            thisList.append(1)
            for j in range(1, len(lastList)):
                thisList.append(lastList[j-1] + lastList[j])
            thisList.append(1)
            lastList = thisList
        return lastList

s = Solution()
print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)
print s.getRow(5)
print s.getRow(6)