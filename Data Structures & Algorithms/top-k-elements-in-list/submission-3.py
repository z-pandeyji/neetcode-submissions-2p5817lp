class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      match = {}
      for i in nums:
        if i not in match:
          match[i] = 1
        else:
          match[i] += 1
      pairs = []
      for key in match:
        pairs.append([key, match[key]])
      print(pairs)
      pairs.sort(key= lambda x: x[1], reverse=True)
      print(pairs)
      result = []
      for i in range(k):
        print(pairs[i])
        result.append(pairs[i][0])

      return result

      
        
