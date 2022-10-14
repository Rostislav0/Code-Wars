def longest(a1, a2):
    s = a1 + a2
    s_s = sorted(set(s))
    return ''.join(s_s)


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))