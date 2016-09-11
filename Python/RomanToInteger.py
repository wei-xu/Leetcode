def romanToInt(s):
    mapRomanInt = dict()
    mapRomanInt['I'] = 1
    mapRomanInt['V'] = 5
    mapRomanInt['X'] = 10
    mapRomanInt['C'] = 100
    mapRomanInt['L'] = 50
    mapRomanInt['D'] = 500
    mapRomanInt['M'] = 1000
    mapRomanInt['IV'] = 4
    mapRomanInt['IX'] = 9
    mapRomanInt['XL'] = 40
    mapRomanInt['XC'] = 90
    mapRomanInt['CD'] = 400
    mapRomanInt['CM'] = 900
    output_sum = 0
    index = 0
    while index < len(s):
        if index + 1 < len(s):
            combo = s[index] + s[index + 1]
            if combo in mapRomanInt:
                output_sum += mapRomanInt[combo]
                index += 2
            else:
                output_sum += mapRomanInt[s[index]]
                index += 1
        else:
            output_sum += mapRomanInt[s[index]]
            index += 1
    return output_sum

print romanToInt("MCMLIV")
print romanToInt("MCMXC")
print romanToInt("MMXIV")
print romanToInt("DCXXI")