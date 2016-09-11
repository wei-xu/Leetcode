import collections
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = {x: [] for x in range(n)}
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        queue = collections.deque()
        queue.append(0)
        while len(queue) > 0:
            node = queue.popleft()
            if node not in graph:
                continue
            queue.extend(graph[node])
            del graph[node]
        if len(graph) == 0:
            return len(edges) < n
        else:
            return False



s = Solution()
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
edges3 = [[0, 1], [0, 2], [1, 2]]
print s.validTree(5, edges)
print s.validTree(5, edges2)
print s.validTree(4, edges3)