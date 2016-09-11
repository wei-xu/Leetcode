class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = [[] for _ in xrange(numCourses)]
        self.visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            self.graph[x].append(y)

        for i in xrange(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True
        self.visit[i] = -1
        for j in self.graph[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True