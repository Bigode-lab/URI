n = int(input())
for x in range(n):
    a = input()
    led = 0
    for x in a:
        if x == '1':
            led += 2
        elif x == '2' or x == '3' or x == '5':
            led += 5
        elif x == '6' or x == '9' or x =='0':
            led += 6
        elif x == '4':
            led += 4
        elif x == '7':
            led += 3
        elif x == '8':
            led += 7
    print(f'{led} leds')