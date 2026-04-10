class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        max_len = 0
        seen = {}

        for right in range(n):
            ch = s[right]

            if ch in seen:
                prev_index = seen[ch]
                if prev_index >= l:
                    l = prev_index + 1

            seen[ch] = right
            current_len = right - l+1
            if current_len > max_len:
                max_len = current_len
            
        return max_len

        