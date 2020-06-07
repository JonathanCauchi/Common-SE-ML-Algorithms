
lines = []
while(True):
    a = str(input('Enter sentence\n'))
    if a:
        lines.append(a.upper())
    else:
        break

for i in lines:
    print(i)