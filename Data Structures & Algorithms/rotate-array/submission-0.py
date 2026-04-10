class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if k > n:
            k = k % n
        def revArray(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        # def revArray(arr, start, end):
        #     arr[start:end] = arr[start:end][::-1]
        revArray(nums, 0, n-1)
        revArray(nums, 0, k-1)
        revArray(nums, k, n-1)


        