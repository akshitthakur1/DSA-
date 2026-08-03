class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = -1
        k = len(s)
        while i>= (-1*k) and s[i] !=" ":
            i-=1
        i += 1
        i *= -1
        return i    

        