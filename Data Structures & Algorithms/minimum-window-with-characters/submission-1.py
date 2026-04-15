class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        formed = 0
        required = len(need)
        result = ""
        l = 0
        
        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1
            
            while formed == required:
                window = s[l:r+1]
                if result == "" or len(window) < len(result):
                    result = window
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return result
        