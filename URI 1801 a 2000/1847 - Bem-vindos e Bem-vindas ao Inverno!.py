tp1 ,tp2, tp3 = (int(x) for x in input().split())

if tp1> tp2 and ((tp2 < tp3) or (tp3 == tp2)):
    print(':)')
elif tp1< tp2 and ((tp2 == tp3) or (tp2 > tp3)):
    print(':(')
elif tp1< tp2 and tp2 < tp3 and (tp2 - tp1) > (tp3 - tp2):
    print(':(')
elif tp1< tp2 and tp2 < tp3 and (tp3 - tp2) >= (tp2 - tp1):
    print(':)')
elif tp1> tp2 and tp2 > tp3 and (tp1- tp2) > (tp2 - tp3):
    print(':)')
elif tp1> tp2 and tp2 > tp3 and (tp1- tp2) <= (tp2 - tp3):
     print(':(')
elif tp1== tp2 and tp2 < tp3:   
    print(':)')
elif tp1== tp2 and tp2 > tp3:
    print(':(')
else:
    print(':(')