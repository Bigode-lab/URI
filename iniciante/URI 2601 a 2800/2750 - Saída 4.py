import time
tinicial = time.time()
print(39*'-')
print('| decimal   |  octal  |  Hexadecimal  |')
print(39*'-')
for x in range(8):
    a = str(oct(x))
    h = str(hex(x))
    print(f'|      {x}    |    {a[-1]}    |       {h[-1]}       |')
for x in range(8, 10):
    a = str(oct(x))
    h = str(hex(x))
    print(f'|      {x}    |   {a[-2:]}    |       {h[-1]}       |')
for x in range(10, 16):
    a = str(oct(x))
    h = str(hex(x))
    print(f'|     {x}    |   {a[-2:]}    |       {(h[-1]).upper()}       |')
print(39*'-')
final = time.time()
total = final - tinicial
print(f'{total}')
