class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = collections.defaultdict(int)
        for n in nums:
            f[n] += 1
        frequencies = [""] * len(nums)
        for key, v in f.items():
            if frequencies[v - 1] == "":
                frequencies[v - 1] = [key]
            else:
                frequencies[v - 1].append(key)


        fs = []
        for f in frequencies:
            if f != "":
                for a in f:
                    fs.append(a)

        output = []
        for i in range(k):
            output.append(fs.pop())

     
        return output
    