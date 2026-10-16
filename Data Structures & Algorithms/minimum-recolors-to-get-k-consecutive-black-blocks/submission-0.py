class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0

        # Count whites in the first group of k blocks.
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1

        minimum = whites
        # Slide the group one position at a time.
        for right in range(k, len(blocks)):
            # Remove the block leaving the group.
            if blocks[right - k] == 'W':
                whites -= 1

            # Add the block entering the group.
            if blocks[right] == 'W':
                whites += 1

            minimum = min(minimum, whites)

        return minimum