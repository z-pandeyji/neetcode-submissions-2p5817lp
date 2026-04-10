class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            maxArea = max(maxArea,area)
            print(maxArea)
            print('a')
            if heights[l] < heights[r]:
                l+=1
                print('l+1')
                print(l)
            else:
                r -= 1
                print('r+1')
                print(r)
        return maxArea
        