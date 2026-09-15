class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            a = str(sorted(string))
            if a not in anagrams:
                anagrams[a] = [string]
            else:      
                anagrams[a].append(string)
          
        return list(anagrams.values())