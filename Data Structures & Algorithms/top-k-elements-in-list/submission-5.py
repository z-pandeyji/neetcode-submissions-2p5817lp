class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      freq = {}
      for num in nums:
        if num not in freq:
          freq[num] = 1
        else:
          freq[num] += 1

      n = len(nums)
      bucket = [[] for _ in range(n+1)]

      for key, f in freq.items():
        bucket[f].append(key)
      result = []
      for f in range(n, -1, -1):
        for val in bucket[f]:
          result.append(val)
          if len(result) == k:
            return result
      
      return result

      
        
