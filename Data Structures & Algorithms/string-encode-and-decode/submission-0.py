class Solution:

    def encode(self, strs: List[str]) -> str:
      hashed = ""
      for i in strs:
        hashed += str(len(i))+'#'+i
      return hashed
        

    def decode(self, s: str) -> List[str]:
      result = []
      i = 0
      n = len(s)
      while i < n:
        l = 0
        while i < n and s[i] != '#':
          digit = ord(s[i]) - ord('0')
          l = l * 10 + digit
          i += 1
        i += 1
        char = []
        count = 0
        while count < l:
          char.append(s[i])
          i += 1
          count += 1
        word = "".join(char)
        result.append(word)
      return result

