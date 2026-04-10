class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(n):
            ch = s[right]
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            if freq[ch] > max_freq:
                max_freq = freq[ch]
            window_len = right - left + 1

            if window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                window_len -= 1
            if window_len > max_len:
                max_len = window_len
            
        return max_len


        