class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        l_max = 0
        r_max = 0
        water = 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] < l_max:
                    water += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if height[r] < r_max:
                    water += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return water