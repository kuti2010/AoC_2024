import numpy as np
import re

# Task 1, 31065, 1 - 9 tarkkuudella

path = ['2024_13\\test.txt', '2024_13\\input.txt']

A = []
B = []
P = []
A_b = 3
B_b = 1
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
    b = np.array([int(P[n][0][0]), int(P[n][0][1])])
    sol = np.linalg.solve(a, b)
    sol_a = round(sol[0], 2)
    sol_b = round(sol[1], 2)
    if sol_a == int(sol_a) and sol_b == int(sol_b) and sol_a <= 100 and sol_b <= 100:
        summa += (A_b*sol_a + B_b*sol_b)

print(summa)