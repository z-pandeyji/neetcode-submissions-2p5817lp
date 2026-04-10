class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      m_str = ""
      char = min(len(word1), len(word2))
      for i in range(char):
        ch1 = word1[i]
        ch2 = word2[i]
        m_str += ch1 + ch2
      if len(word1) >= len(word2):
        m_str += word1[char::]
      elif len(word1) <= len(word2):
        m_str += word2[char::]
      return m_str
        
     