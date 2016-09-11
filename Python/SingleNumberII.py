class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [0] * 32
        for num in nums:
            binary_str = bin(num)[2:]
            binary = map(int, [binary_str[x] for x in range(len(binary_str))])
            for i in range(len(binary)):
                memory[len(memory) - i - 1] += binary[len(binary) - i - 1]
        pos = -1
        for idx in range(len(memory)):
            memory[idx] %= 3
            if memory[idx] != 0 and pos == -1:
                pos = idx

        new_memory = memory[pos:]
        for n in range(len(new_memory)):
            if new_memory[n] == 2:
                new_memory[n] = 1
        order = 0
        sum = 0
        for i in range(len(new_memory) - 1, -1, -1):
            sum += new_memory[i] * 2 ** order
            order += 1
        return sum

s = Solution()
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print s.singleNumber(nums)