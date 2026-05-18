class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in ["!", "?", ".", " ", ",", "'", ":"]:
            s = s.replace(i, "")
        s = s.lower() #wasitacarorcatisaw
        if s[::-1] == s: #tabacat
            return True
        return False