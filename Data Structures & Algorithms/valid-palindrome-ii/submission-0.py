class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                i,j = l+1, r
                while (i < j) and s[i] == s[j]:
                    i += 1
                    j -= 1
                if (i >= j):
                    return True
                i,j = l, r-1
                while (i < j) and s[i] == s[j]:
                    i += 1
                    j -= 1
                if(i >= j):
                    return True
                return False
            l += 1
            r -= 1
        return True
        

        