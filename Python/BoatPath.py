class Solution:
    def boatPath(self, terrain_map, water_level):
        self.paths = []
        self.dfs(terrain_map, water_level, 0, 0, [])
        return self.paths

    def dfs(self, terrain_map, water_level, i, j, path):
        # if hit borders
        if i < 0 or j < 0 or i >= len(terrain_map) or j >= len(terrain_map[0]):
            return
        if terrain_map[i][j] > water_level:
            return
        if i == len(terrain_map) - 1 and j == len(terrain_map[0]) - 1:
            path.append((i, j))
            self.paths.append(path)
            return
        if (i, j) in path:
            return
        new_path = path + [(i, j)]
        self.dfs(terrain_map, water_level, i + 1, j, new_path)
        self.dfs(terrain_map, water_level, i, j + 1, new_path)
        self.dfs(terrain_map, water_level, i - 1, j, new_path)
        self.dfs(terrain_map, water_level, i, j - 1, new_path)


terrain_map = [
    [0, 2, 6, 4],
    [2, 9, 6, 8],
    [3, 4, 3, 4],
    [4, 3, 5, 1],
]
s = Solution()
print s.boatPath(terrain_map, 4)