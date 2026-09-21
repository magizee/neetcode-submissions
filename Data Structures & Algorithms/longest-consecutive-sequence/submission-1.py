class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        heads = []
        for n in nums:
            if n - 1 not in nums:
                heads.append(n)
        
        max_length = 0
        for head in heads:
            length = 1
            while head + 1 in nums:
                length += 1
                head += 1
            max_length = max(length, max_length)
        return max_length