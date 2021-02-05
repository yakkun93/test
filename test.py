"""

f = open('.input.txt', 'r')

list = []
for line in f:
    list.append(line)

m = int(list[-1])
list.pop()

dict = {}
for x in list:
    x1 = int(x.split(':')[0])
    x2 = x.split(':')[1].strip()
    dict[x2] = x1
dict_val = dict.values()

dict_val2 = []
for x in dict_val:
    if m % x == 0:
        dict_val2.append(x)
dict_val2.sort()
list2 = []
for x, y in dict.items():
    if y in dict_val2:
        list2.append(x)

ans = ''.join(list2)
print(ans)
"""
