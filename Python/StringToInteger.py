class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        output = ''
        for i in range(len(str)):
            if str[i].isdigit():
                output += str[i]
            elif (str[i] == '-' or str[i] == '+') and output == '':
                output += str[i]
            else:
                break
        if output == '' or output == '-' or output == '+':
            return 0
        else:
            output_int = int(output)
            if output_int > 0:
                return min(2147483647, output_int)
            elif output_int < 0:
                return max(-2147483648, output_int)
            else:
                return 0

s = Solution()
print s.myAtoi("12")  # pure integer
print s.myAtoi("-")  # minus symbol
print s.myAtoi("ab")  # non-numeric char
print s.myAtoi("ab123")  # numeric and non-num
print s.myAtoi("123ab")  # num and non-num
print s.myAtoi("-123ab")  # num / non-num neg
print s.myAtoi("-a123b")  # ??
print s.myAtoi("+1")
print s.myAtoi("+-1")
print s.myAtoi("+2aab3")
print s.myAtoi("+23.45")
print s.myAtoi("2147483648")