class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        lengths = []
        for s in strs:
            lengths.append(str(len(s)))
        
        print("encode: " + ",".join(lengths) + chr(257) + "".join(strs))
        return ",".join(lengths) + chr(257) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        size, strings = s.split(chr(257))
        sizes = size.split(",")
        print(sizes)
        print(strings)
        i = 0
        output = []
        for sz in sizes:
            output.append(strings[i:i+int(sz)])
            i+= int(sz)
        return output
