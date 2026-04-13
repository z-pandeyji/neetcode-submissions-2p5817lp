class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c,0) + 1
        
        for c in t:
            hashmap[c] = hashmap.get(c,0) -1
        
        for val in hashmap.values():
            if val != 0:
                return False
        return True
        