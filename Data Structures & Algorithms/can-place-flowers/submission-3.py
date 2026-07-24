class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 1
        
        for f in flowerbed:
            if f == 1:
                n -= int((empty - 1) // 2)
                empty = 0
            else:
                empty += 1
        
        n -= empty // 2
        return n <= 0