
class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        # Sum of all elements in the top row
        top_sum = sum(grid[0])

        bottom_sum = 0
        answer = float('inf')

        for j in range(len(grid[0])):
            # Robot 1 has cleared top row up to j
            top_sum -= grid[0][j]

            # Robot 2 selects the larger remaining sum
            second_robot = max(top_sum, bottom_sum)

            # Robot 1 selects the smallest possible score
            answer = min(answer, second_robot)

            # Add current bottom cell for future columns
            bottom_sum += grid[1][j]

        return answer
