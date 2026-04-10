class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = None
        num2 = None
        count1 = 0
        count2 = 0
        for x in nums: 
            if num1 is not None and x == num1:
                count1 += 1
            elif num2 is not None and x == num2:
                count2 += 1
            elif count1 == 0:
                num1 = x
                count1 = 1
            elif count2 == 0:
                num2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        print(num1, count1)
        print(num2, count2)
        result = []
        freq1, freq2 = 0, 0
        for x in nums:
            if num1 is not None and x == num1:
                freq1 += 1
            if num2 is not None and x == num2:
                freq2 += 1
        n = len(nums)
        if freq1 > n // 3:
            result.append(num1)
        if num2 != num1 and freq2 > n // 3:
            result.append(num2)
        return result 
        