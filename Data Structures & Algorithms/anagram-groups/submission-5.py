class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            count = tuple(count)
            if count not in m:
                m[count] = [string]
            else:
                m[count].append(string)
        return list(m.values())