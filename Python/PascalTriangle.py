class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = list()
        output.append([1])
        output.append([1,1])
        lastList = [1,1]
        if numRows == 0:
            return []
        if numRows == 1:
            return output[:1]
        for i in range(3, numRows + 1):
            thisList = list()
            thisList.append(1)
            for j in range(1, len(lastList)):
                thisList.append(lastList[j-1] + lastList[j])
            thisList.append(1)
            output.append(thisList)
            lastList = thisList
        return output

s = Solution()
print s.generate(0)
print s.generate(1)
print s.generate(2)
print s.generate(3)
