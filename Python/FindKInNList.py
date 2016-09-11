import sys
class Solution:
    def findK(self, arrays, k):
        '''
        return the smallest k element in n arrays
        :param arrays: List[List[int]]
        :return: List[int]
        '''
        output = []
        l = len(arrays)
        indexes = [0] * l
        for _ in range(k):
            t = [arrays[i][indexes[i]] if indexes[i] != -1 else sys.maxint for i in range(l)]
            m = min(t)
            output.append(m)
            choose_from = t.index(m)
            if indexes[choose_from] == len(arrays[choose_from]) - 1:
                indexes[choose_from] = -1
            else:
                indexes[choose_from] += 1
        return output

s = Solution()
nums = [
    [1, 4, 3],
    [1, 2, 3],
    [1, 3, 6],
]
print s.findK(nums, 6)