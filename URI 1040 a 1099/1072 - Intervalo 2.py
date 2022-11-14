den = 0
out = 0
n = int(input())
for x in range(n):
    num = int(input())
    if num >= 10 and num <= 20:
        den += 1
    else:
        out += 1
print('{} in'.format(den))
print('{} out'.format(out))