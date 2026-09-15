class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output_index = -1
        output = []
        for string in strs:
            a = str(sorted(string))
            if a not in anagrams:
                output_index += 1
                anagrams[a] = output_index
                
                output.append([string])
            else:                
                output[anagrams[a]].append(string)
        return output