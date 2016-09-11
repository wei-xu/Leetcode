import collections
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # faster version
        g = {x: [] for x in range(n)}
        for s, t in edges:
            g[s].append(t)
            g[t].append(s)

        components = 0
        for i in range(n):
            queue = [i]
            components += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]
        return components


        # old version

        # graph = collections.defaultdict(list)
        # for s, t in edges:
        #     graph[s].append(t)
        #     graph[t].append(s)
        # components = 0
        # nodes = set(range(n))
        # queue = collections.deque()
        # while len(nodes) > 0:
        #     queue.append(nodes.pop())
        #     nodes.add(queue[-1])
        #     while len(queue) > 0:
        #         node = queue.popleft()
        #         if node not in nodes:
        #             continue
        #         else:
        #             queue.extend(graph[node])
        #             nodes.remove(node)
        #     components += 1
        #     queue.clear()
        # return components

s = Solution()
edges = [[0, 1], [1, 2], [3, 4]]
edges1 = [[0, 1], [1, 2], [2, 3], [3, 4]]
edges2 = [[2, 3], [0, 1], [1, 2], [3, 4]]
print s.countComponents(5, edges2)
