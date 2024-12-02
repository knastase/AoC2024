import re
with open('input.txt', 'r') as f:
    data = f.read()

list1 = []
list2 = []
for line in data.split('\n'):
    i = line.split(' ')
    list1.append(i[0])
    list2.append(i[-1])

list1 = sorted(list1)
list2 = sorted(list2)
diff = 0
for index in range(0, len(list1)):
    diff += abs(int(list1[index]) - int(list2[index]))

print(diff)

similarity = 0
str_list2 = ",".join(list2)
for item in list1:
    matches = re.findall(item, str_list2)
    if matches:
        similarity += int(item) * len(list(matches))
print(similarity)