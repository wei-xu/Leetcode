class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        size = len(nums)
        self.sums = [0] * (size + 1)
        for x in range(size):
            self.sums[x + 1] += self.sums[x] + nums[x]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]

# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.n = nums
#         self.pair = dict()
#         self.memory = dict()
#
#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         if (i, j) in self.memory:
#             return self.memory[(i, j)]
#         sum = 0
#         count = i
#         while count <= j:
#             if count not in self.pair:
#                 sum += self.n[count]
#                 count += 1
#             else:
#                 right_edge = self.pair[count]
#                 index = len(right_edge) - 1
#                 while index >= 0 and right_edge[index] > j:
#                     index -= 1
#                 if index < 0:
#                     sum += self.n[count]
#                     count += 1
#                 else:
#                     t = (count, right_edge[index])
#                     sum += self.memory[t]
#                     count = right_edge[index] + 1
#         if i not in self.pair:
#             self.pair[i] = [j]
#         else:
#             self.pair[i].append(j)
#         self.memory[(i, j)] = sum
#         return sum


# Your NumArray object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numArray = NumArray(nums)
# print numArray.sumRange(0, 1)
# print numArray.sumRange(1, 2)
# print numArray.sumRange(0, 6)

# print numArray.sumRange(0, 7)
# print numArray.sumRange(8, 9)
# print numArray.sumRange(0, 9)
print numArray.sumRange(0, 3)
print numArray.sumRange(4, 9)
print numArray.sumRange(0, 4)
print numArray.sumRange(0, 9)