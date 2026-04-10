class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op not in {"+", "D", "C"}:
                value = int(op)
                scores.append(value)
            elif op == "+":
                last = scores[-1]
                second_last = scores[-2]
                new_score = last + second_last
                scores.append(new_score)
            elif op == "D":
                last = scores[-1]
                new_score = 2 * last
                scores.append(new_score)
            elif op == "C":
                scores.pop();
        total = 0
        for x in scores:
            total += x
        return total