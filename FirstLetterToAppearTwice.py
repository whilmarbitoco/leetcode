class Solution:
    def repeatedCharacter(self, s: str) -> str:

        list = []

        for i in range(len(s)):
            if s[i] in list:
                return s[i]
                
            list.append(s[i])

        return None