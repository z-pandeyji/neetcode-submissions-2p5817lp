class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n = len(nums)
      left = [0] * n
      right = [0] * n
      left[0] = 1
      for i in range(1,n):
        left[i] = left[i-1] * nums[i-1]
      # print(left)
      
      right[-1] = 1
      for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
      # print(right)
      # maxVal = max(len(left), len(right))
      result = []
      for n in range(n):
        result.append(left[n] * right[n])
      return result
      # result = left * right
      # print(result)


        