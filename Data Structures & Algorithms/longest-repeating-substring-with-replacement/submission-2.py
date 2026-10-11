class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char,0) + 1
            max_freq = max(max_freq, freq[char])
            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right-left + 1)
        
        return result
        