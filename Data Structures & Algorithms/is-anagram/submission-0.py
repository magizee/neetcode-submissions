class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in seen_s:
                seen_s[s[i]] = 1
            else:
                seen_s[s[i]] += 1
            if t[i] not in seen_t:
                seen_t[t[i]] = 1
            else:
                seen_t[t[i]] += 1
        print(seen_s)
        print(seen_t)
        if seen_s == seen_t:
            return True
        else:
            return False
