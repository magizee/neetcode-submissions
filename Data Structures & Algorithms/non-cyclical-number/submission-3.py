class Solution:
    def isHappy(self, n: int) -> bool:
        outputs = set()
        n_string = str(n)
        init = 0
        for char in n_string:
            init += int(char) * int(char)
        print(n_string)
        print(init)
        if init == 1:
            return True
        outputs.add(n)
        while init not in outputs:
            if init == 1:
                return True
            else:
                n_string = str(init)
                outputs.add(init)

                init = 0
                for char in n_string:
                    init += int(char) * int(char)
                print(init)
        return False
        