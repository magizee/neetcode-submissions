class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        nums.sort()

        output = set()

        for i in range(len(s)):
            # if i > 0 and s[i] == s[i - 1]: continue
            target = -s[i]
            l = i + 1
            h = len(s) - 1
            while l < h:
                if s[l] + s[h] == target:
                    output.add((s[i], s[l], s[h]))
                    l += 1
                    h -= 1
                elif s[l] + s[h] < target:
                    l += 1
                elif s[l] + s[h] > target:
                    h -= 1
                # while l < h and s[l] == s[l - 1]:
                #     l += 1
                # while l < h and h < len(s) - 1 and s[h] == s[h + 1]:
                #     h -= 1
        return [list(x) for x in output]