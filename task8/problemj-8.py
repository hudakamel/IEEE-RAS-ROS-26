s = input()
res = ""
i = 0

while i < len(s):
    if s[i] == '.':
        res += '0'
        i += 1
    elif s[i:i+2] == '-.':
        res += '1'
        i += 2
    elif s[i:i+2] == '--':
        res += '2'
        i += 2

print(res)