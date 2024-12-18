import re

path = ['2024_17\\test2.txt','2024_17\\input.txt']

with open(path[1],'r') as f:
    for line in f:
        if re.findall(r'A:.(\d+)', line):
            a = re.findall(r'A:.(\d+)', line)
            a = int(a[0])
        elif re.findall(r'B:.(\d+)', line):
            b = re.findall(r'B:.(\d+)', line)
            b = int(b[0])
        elif re.findall(r'C:.(\d+)', line):
            c = re.findall(r'C:.(\d+)', line)
            c = int(c[0])
        elif re.findall(r'm:\s*([\d,]+)', line):
            prog = re.findall(r'm:\s*([\d,]+)', line)
            prog = list(map(int, prog[0].split(',')))

def run(a, b, c, i=0, R=[]):
    while i in range(len(prog)):
        opcode = prog[i]
        operand = prog[i+1]
        if operand == 4: operand = a
        elif operand == 5: operand = b
        elif operand == 6: operand = c
        if opcode == 0: a = int(a//(2**operand))
        elif opcode == 1: b = int(operand ^ b)
        elif opcode == 2: b = int(operand % 8)
        elif opcode == 3: i = operand - 2 if a != 0 else i
        elif opcode == 4: b = b = int(b ^ c)
        elif opcode == 5: R = R + [int(operand % 8)]
        elif opcode == 6: b = int(a//(2**operand))
        elif opcode == 7: c = int(a//(2**operand))
        i += 2
    return R

def find(a, i):
    if run(a, b, c) == prog: print(str(a))
    if run(a, b, c) == prog[-i:] or not i:
        for n in range(8): find(8*a+n, i+1)

print(",".join(map(str, run(a,b,c))))
find(0, 0)