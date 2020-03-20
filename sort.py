a = [1, 2, 3]
b = ['a', 'b', 'c', 'd']
c = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

res = []
count = 0

for i in a:
    for j in b:
        for k in c:
            s = '{}_{}_{}_{}'.format(j, i, k, count)
            #print(s)
            res.append(s)
            count += 1

print(res)
print()

#python approach
print(sorted(res, key=lambda X:X.split('_')[2]))

print()

new_res = []
len_c = len(c)
for i in range(len(c)):
    new_res.extend(res[i::len_c])

print(new_res)