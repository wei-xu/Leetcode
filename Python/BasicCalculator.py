class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        buffer = list()
        num_buffer = ''
        operation = 1
        ans = 0
        s += '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num_buffer += s[i]
            elif s[i] == '+':
                if num_buffer:
                    ans += int(num_buffer) * operation
                    num_buffer = ''
                operation = 1
            elif s[i] == '-':
                if num_buffer:
                    ans += int(num_buffer) * operation
                    num_buffer = ''
                operation = -1
            elif s[i] == '(':
                if num_buffer:
                    ans += int(num_buffer) * operation
                    num_buffer = ''
                buffer.append(ans)
                buffer.append(operation)
                ans = 0
                operation = 1
            elif s[i] == ')':
                if num_buffer:
                    ans += int(num_buffer) * operation
                    num_buffer = ''
                op_before_paren = buffer.pop()
                ans_before_paren = buffer.pop()
                ans = ans_before_paren + ans * op_before_paren
        return ans


s = Solution()
string1 = ''
string2 = '2'
string3 = '1 + 1'
string4 = ' 2-1 + 2 '
string5 = '(1+(4+5+2)-3)+(6+8)'
string6 = '2-(5-6)'
print s.calculate(string1)
print s.calculate(string2)
print s.calculate(string3)
print s.calculate(string4)
print s.calculate(string5)
print s.calculate(string6)