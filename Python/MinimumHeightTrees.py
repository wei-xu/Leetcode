import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        nodes = collections.defaultdict(set)
        for s, t in edges:
            nodes[s].add(t)
            nodes[t].add(s)
        # vertices = set(nodes)
        while len(nodes) > 2:
            leaves = [x for x in nodes if len(nodes[x]) == 1]
            for node in leaves:
                for y in nodes[node]:
                    nodes[y].remove(node)
                del nodes[node]
        return nodes.keys() if n != 1 else [0]


    # def findMinHeightTrees(self, n, edges):
    #     """
    #     :type n: int
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     if n == 1:
    #         return [0]
    #     self.connection = dict()
    #     self.leaf_node = set()
    #     self.paths = []
    #     for edge in edges:
    #         if edge[0] in self.connection:
    #             self.connection[edge[0]].append(edge[1])
    #         else:
    #             self.connection[edge[0]] = [edge[1]]
    #         if edge[1] in self.connection:
    #             self.connection[edge[1]].append(edge[0])
    #         else:
    #             self.connection[edge[1]] = [edge[0]]
    #     for key in self.connection:
    #         if len(self.connection[key]) == 1:
    #             self.leaf_node.add(key)
    #     self.bfs()
    #     longest = max(self.paths, key=len)
    #     if len(longest) % 2 == 0:
    #         return [longest[(len(longest) - 1)/2], longest[(len(longest) - 1)/2 + 1]]
    #     else:
    #         return [longest[(len(longest) - 1)/2]]
    #
    # def bfs(self):
    #     path = []
    #     for i in self.leaf_node:
    #         queue = deque()
    #         queue.append(i)
    #         while queue:
    #             node = queue.popleft()
    #             if node in path:
    #                 continue
    #             path.append(node)
    #             if node in self.leaf_node and node != i:
    #                 self.paths.append(path)
    #                 path = list(path)
    #                 path.pop()
    #             queue += self.connection[node]

s = Solution()
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
edges1 = [[1, 0], [1, 2], [1, 3]]
edges2 = []
edges3 = [[0, 1]]
n = 6
print s.findMinHeightTrees(4, edges1)
print s.findMinHeightTrees(1, edges2)
print s.findMinHeightTrees(2, edges3)