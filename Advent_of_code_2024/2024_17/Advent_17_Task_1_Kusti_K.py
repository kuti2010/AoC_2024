import re

def select(operand):
    if operand == 4:
        operand = A
    elif operand == 5:
        operand = B
    elif operand == 6:
        operand = C
    return operand

def adv(operand,A): # 0
    A = int(A//(2**operand))
    return A

def bxl(operand,B): # 1
    B = int(operand ^ B)
    return B

def bst(operand,B): # 2
    B = int(operand % 8)
    return B

def jnz(i,operand): # 3
    i = operand
    return i

def bxc(B,C): # 4
    B = int(B ^ C)
    return B

def out(operand,output): # 5
    output.append(int(operand % 8))
    return output

path = ['2024_17\\test.txt','2024_17\\input.txt']

with open(path[0],'r') as f:
    for line in f:
        if re.findall(r'A:.(\d+)', line):
            A = re.findall(r'A:.(\d+)', line)
            A = int(A[0])
        elif re.findall(r'B:.(\d+)', line):
            B = re.findall(r'B:.(\d+)', line)
            B = int(B[0])
        elif re.findall(r'C:.(\d+)', line):
            C = re.findall(r'C:.(\d+)', line)
            C = int(C[0])
        elif re.findall(r'm:\s*([\d,]+)', line):
            P = re.findall(r'm:\s*([\d,]+)', line)
            P = list(map(int, P[0].split(',')))

output = []
i = 0

while i < len(P):
    opcode = P[i]
    operand = P[i+1]
    operand = select(operand)
    if opcode == 0:
        A = adv(operand,A)
        i += 2
    elif opcode == 1:
        B = bxl(P[i+1],B)
        i += 2
    elif opcode == 2:
        B = bst(operand,B)
        i += 2
    elif opcode == 3:
        if not A == 0:
            i = jnz(i,P[i+1])
        else:
            i += 2
    elif opcode == 4:
        B = bxc(B,C)
        i += 2
    elif opcode == 5:
        output = out(operand,output)
        i += 2
    elif opcode == 6:
        B = adv(operand,A)
        i += 2
    elif opcode == 7:
        C = adv(operand,A)
        i += 2

str = ','.join(str(x) for x in output)
print(str)