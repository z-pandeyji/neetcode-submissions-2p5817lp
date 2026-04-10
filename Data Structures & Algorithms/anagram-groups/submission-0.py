class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      group = {}
      for words in strs:
        s1 = sorted(words)
        key = ''.join(s1)
        if key not in group:
          group[key] = []
        group[key].append(words)
      return list(group.values())
      # result = []
      # for key in group:
      #   result.append(group[key])
      # return result