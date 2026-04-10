class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = [0] * 128
        freq_s = [0] * 128

        need = 0
        for ch in t:
            idx = ord(ch)
            if freq_t[idx] == 0:
                need += 1
            freq_t[idx] += 1
        have = 0
        left = 0

        min_len = 10 ** 10 
        min_start = 0

        for right in range(len(s)):
            r_char = s[right]
            r_idx = ord(r_char)
            freq_s[r_idx] += 1

            if freq_s[r_idx] == freq_t[r_idx] and freq_t[r_idx] > 0:
                have += 1
            while have == need:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = left 
                l_char = s[left]
                l_idx = ord(l_char)
                freq_s[l_idx] -= 1
                if freq_s[l_idx] < freq_t[l_idx] and freq_t[l_idx] > 0:
                    have -= 1
                left += 1
        if min_len == 10**10:
            return ""
        return s[min_start : min_start + min_len]
        