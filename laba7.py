import numpy as np

f = open('1.txt')
s = f.readlines()
a = np.matrix('[3, 4, 17, -3; 5, 11, -1, 6; 0, 2, -5, 8]')

max_ = a.max()
min_ = a.min()
sum_ = a.sum()

'''start = 0
finish = len(s[0])

for i in range(len(s)):
    for j in range(len(s[i])):
        s[i] = str(s[i])
        finish = s[i].find(',', start, finish)

        if finish == -1:
            finish = len(s[i])
        a[i][j] = s[i][start:finish]
        start = finish + 1
        finish = len(s[0])


'''
print(a,max_, min_, sum_)

f.close()

b = np.array([1, 1, 1, 2, 2, 2, 4])

nums = np.empty(0)
counts = np.empty(0)
for i in b:
    if not(i in nums):
        nums = np.append(nums, i)

counter = 0
for i in nums:
    counter = 0
    for j in b:
        if i == j:
            counter += 1

    counts = np.append(counts, counter)

print(nums, counts)


