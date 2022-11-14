t = 0
c = 0
s = 0
r = 0
n = int(input())
for x in range(n):
    a = [str(y) for y in input().split(' ')]
    n1 = int(a[0])
    t += n1
    if a[1] == 'C':
      c += n1
    elif a[1] == 'S':
      s += n1
    elif a[1] == 'R':
      r += n1
pc = (c*100)/t
ps = (s*100)/t
pr = (r*100)/t
print('Total: {} cobaias'.format(t))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))