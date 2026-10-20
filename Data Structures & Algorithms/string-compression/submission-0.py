
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            current = chars[read]
            start = read

            while read < n and chars[read] == current:
                read += 1

            count = read - start

            chars[write] = current
            write += 1

            if count > 1:
                divisor = 1

                while count // divisor >= 10:
                    divisor *= 10

                while divisor > 0:
                    digit = (count // divisor) % 10
                    chars[write] = chr(ord('0') + digit)
                    write += 1
                    divisor //= 10

        return write
