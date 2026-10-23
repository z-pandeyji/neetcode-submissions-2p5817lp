
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        size = 1 << n

        # Store palindrome length for each mask
        pal_len = [0] * size

        # Generate every nonempty subsequence
        for mask in range(1, size):
            subseq = ""

            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]

            # Check if it is a palindrome
            if subseq == subseq[::-1]:
                pal_len[mask] = len(subseq)

        # Find two disjoint palindromes
        ans = 0
        full_mask = size - 1

        for mask in range(1, size):
            if pal_len[mask] == 0:
                continue

            remaining = full_mask ^ mask
            sub = remaining

            while sub:
                if pal_len[sub] > 0:
                    product = pal_len[mask] * pal_len[sub]
                    ans = max(ans, product)

                sub = (sub - 1) & remaining

        return ans
