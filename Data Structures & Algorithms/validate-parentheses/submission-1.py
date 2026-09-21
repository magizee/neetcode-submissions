class Solution:
    def isValid(self, s: str) -> bool:
        setup = {")" : "(", "]": "[", "}": "{"}
        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] not in setup:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    stack.append(s[i])
                elif stack.pop() != setup[s[i]]:
                    return False
            print(stack)
        
        if stack != []:
            return False
        else:
            return True

