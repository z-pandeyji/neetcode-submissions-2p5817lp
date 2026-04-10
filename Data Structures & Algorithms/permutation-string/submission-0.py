class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            index = ord(ch) - ord('a')
            count1[index] += 1
        left = 0

        for right in range(n2):
            r_index = ord(s2[right]) - ord('a')        
            count2[r_index] += 1
            window_len = right - left + 1
            if window_len > n1:
                l_index = ord(s2[left]) - ord('a')
                count2[l_index] -= 1
                left += 1
                window_len -= 1
            if window_len == n1:
                same = True
                for i in range(26):
                    if count1[i] != count2[i]:
                        same = False
                        break
                if same:
                    return True
        return False