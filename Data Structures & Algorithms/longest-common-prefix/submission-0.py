class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return 
        prefix = ""
        first = strs[0]
        n = len(strs)
        for i in range(len(first)):
            char = first[i]
            for j in range(1,n):
                print(j)
                if i>=len(strs[j]):
                    print(f"i is smaller than {strs[j]} and {prefix}")
                    return prefix
                if strs[j][i] != char:
                    print(f"i is not equal {char} to {strs[j][i]} and {prefix}")
                    return prefix
            prefix += char
            print(f"{prefix} and {char}")
        return prefix
        