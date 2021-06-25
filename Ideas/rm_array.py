l1 = -3
r1 = 4
t1 = -2
b1 = 3
l2 = -4
r2 = 5
t2 = -5
b2 = 5
a = [[0 for i in range(r1 - l1)] for j in range(b1 - t1)]
b = [[0 for i in range(r2 - l2)] for j in range(b2 - t2)]
a[3][3] = 1
a[2][1] = 1
a[0][2] = 1
a[4][1] = 1
a[3][2] = 1   
for i in a:
    print(*i)
for i in b:z
    print(*i)


