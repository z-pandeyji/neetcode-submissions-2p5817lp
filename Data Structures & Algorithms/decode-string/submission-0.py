class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []

        current_num = 0
        current_string = ""

        n = len(s)
        i = 0

        while i < n:
            ch = s[i]

            if ch >= "0" and ch <= "9":
                current_num = current_num * 10 + (ord(ch) - ord('0'))

            elif ch == "[":
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0 
                current_string = ""

            elif ch == "]":
                repeat = count_stack.pop()
                prev_string = string_stack.pop()

                expend = ""
                for _ in range(repeat):
                    expend += current_string
                current_string = prev_string + expend
            else:
                current_string += ch
            
            i += 1
        return current_string


        