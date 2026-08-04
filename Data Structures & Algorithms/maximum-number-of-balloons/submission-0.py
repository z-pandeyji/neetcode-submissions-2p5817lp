class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)

        baloon = Counter("balloon")

        res = len(text)
        for c in baloon:
            res = min(res, countText[c] // baloon[c])
        return res
        