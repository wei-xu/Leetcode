class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        output = []
        position = {}
        remain = 0
        start = -1
        count = 0
        while True:
            remain = numerator % denominator
            quota = numerator / denominator
            if remain == 0:
                output.append(quota)
                break
            elif remain in position:
                output.append(quota)
                start = position[remain]
                break
            else:
                output.append(quota)
                position[remain] = count
                numerator = remain * 10
            count += 1
        out = '-' if negative else ''
        output = map(str, output)
        if start == -1:
            out += str(output[0])
            if len(output) != 1:
                out += '.' + ''.join(output[1:])
        else:
            out += str(output[0]) + '.'
            parentheses = ''.join(output[start + 1:])
            before_para = ''.join(output[1: start + 1])
            out += before_para + '(' + parentheses + ')'
        return out

s = Solution()
print s.fractionToDecimal(1, 17)
