import numpy as np
import re

# Task 2, 93 866 170 395 343, 3 or 4
# Too low = 49 634 668 978 096, 9
# Too low = 57 694 128 545 814, 5
# Too high = 160 345 863 082 524, 0

path = ['2024_13\\test.txt', '2024_13\\input.txt']

A = []
B = []
P = []
A_b = 3
B_b = 1
opt = 10000000000000
summa = 0

with open(path[1]) as f:
    for line in f:
        if re.findall(r'Button A:.*X([+-]?\d+), Y([+-]?\d+)',line):
            A.append(re.findall(r'Button A:.*X([+-]?\d+), Y([+-]?\d+)',line))
        elif re.findall(r'Button B:.*X([+-]?\d+), Y([+-]?\d+)',line):
            B.append(re.findall(r'Button B:.*X([+-]?\d+), Y([+-]?\d+)',line))
        elif re.findall(r'X=([+-]?\d+), Y=([+-]?\d+)',line):
            P.append(re.findall(r'X=([+-]?\d+), Y=([+-]?\d+)',line))


for n in range(len(A)):
    a = np.array([[int(A[n][0][0]), int(B[n][0][0])], [int(A[n][0][1]), int(B[n][0][1])]])
    b = np.array([(int(P[n][0][0])+opt), (int(P[n][0][1])+opt)])
    sol = np.linalg.solve(a, b)
    sol_a = round(sol[0],2)
    sol_b = round(sol[1],2)
    if sol_a == int(sol_a) and sol_b == int(sol_b):
        summa += (A_b*sol_a + B_b*sol_b)

print(summa)