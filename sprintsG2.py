#Primary G2 Sprint Lux2019

import random as rd
a = 0
b = 0
c = 0
count = 0
total_count = 0
count_line = 0
plus_sub_max = 0
mul_div_max = 0

total_count = int(round(float(input('总共输出多（上）少（百）题（万）:  ')), 0))
count_line = int(round(float(input('每行多（小）少（几）题（千）？:  ')), 0))
plus_sub_max = int(round(float(input('输出几（千万）以内的加减法？:  ')), 0))
mul_div_max = int(round(float(input('输出几（亿）以内的乘除法？:    ')), 0))

#print(total_count, count_line, plus_sub_max, mul_div_max)

def plus_sub(a,b):
    if a > b and a+b< plus_sub_max:
        return("{0} + {1} = ".format( a, b))
    elif a <= b and b-a>=0:
        return ("{0} - {1} = ".format(b, a))

def multply(a,b):
    if a*b < mul_div_max:
        return("{0} x {1} = ".format(a, b))

def divide(a,b):
    if a != 0 and a*b < mul_div_max:
        return ("{0} ÷ {1} = ".format(a*b, a))

for i in range(10000):
    c = rd.randint(1,3)
    if c == 1 and count < total_count:
        a = rd.randint(10, 100)
        b = rd.randint(10,100)
        if plus_sub(a,b):
            print(plus_sub(a,b), end='\t\t')
            count += 1
            if count % count_line == 0:
                print('\r')
    if c == 2 and count < total_count:
        a = rd.randint(2, 10)
        b = rd.randint(2, 10)
        if multply(a, b):
            print(multply(a, b), end='\t\t')
            count += 1
            if count % count_line == 0:
                print('\r')
    if c == 3 and count < total_count:
        a = rd.randint(2, 10)
        b = rd.randint(2, 10)
        if divide(a, b):
            print(divide(a, b), end='\t\t')
            count += 1
            if count % count_line == 0:
                print('\r')
