class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
        if len(v1) == len(v2):
            return 0
        if len(v1) > len(v2):
            for idx in range(len(v2), len(v1)):
                if not v1[idx] == 0:
                    return 1
        else:
            for idx in range(len(v1), len(v2)):
                if not v2[idx] == 0:
                    return -1
        return 0

s = Solution()
print s.compareVersion('1.1.1', '1.1.1')
print s.compareVersion('1.1', '1.1.1')
print s.compareVersion('1.1.1', '1.1.1.0.0')
print s.compareVersion('1.1.1', '1.1.1.0.1')
print s.compareVersion('1', '1.0')
print s.compareVersion('1.1.13', '1.12.1')
print s.compareVersion('1.11.1', '1.1.1')
print s.compareVersion('1', '1.1')