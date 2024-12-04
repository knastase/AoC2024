import re

with open('input.txt', 'r') as f:
    data = f.read()

print(f'\nPART 1:')

m = re.findall('mul\((?P<first>\d+)\,(?P<second>\d+)\)', data)
if m:
    total = 0
    for a in m:
        total += int(a[0]) * int(a[1])
    
print(total)

print(f'\nPART 2:')
total = 0
do = True
i = 0
while i < len(data):
    # print(data[i:i+12])
    m = re.search('do\(\)', data[i:i+4])
    if not m:
        m = re.search('don\'t\(\)', data[i:i+7])
        if not m:
            m = re.search('mul\((?P<first>\d+)\,(?P<second>\d+)\)', data[i:i+12])
            if m and do:
                total += int(m.group('first')) * int(m.group('second'))
                print(total)
                i += len(m.group(0))
            elif m:
                i += len(m.group(0))
            else:
                i += 1
        else:
            print('don\'t()')
            do = False
            i += 7
    else:
        print('do()')
        do = True
        i += 4

print(total)