#1015
#seconds = int(input())
#print(seconds//60)

#1016
#a,b = map(int, input().split())
#print(a - (a // b) * b)

#1017

#x = int(input())
#if x % 2 == 0:
#    print("Yes")
#else:
#    print("No")

#1018
#a,b = map(int, input().split())
#if a > b:
#    print(a*2)
#else:
#    print(b*2)

#1019
#a = int(input())
#if a %2 == 0:
#    print(int(a / 2))
#else:
#    print(0)

#1020
#a,b = map(int, input().split())
#if b > a:
#    print(a,b)
#else:
#    print(b,a)

#1021
#p = float(input())
#if p % 1 == 0:
#    print("Yes")
#else:
#    print("No")

#1022
#a,b,c,d = map(int, input().split())
#min,max = 0,0
#if a>b and a>c and a>d:
#    max = a
#elif b>a and b>c and b>d:
#    max = b
#elif c>a and c>b and c>d:
#    max = c
#elif d>a and d>c and d>c:
#    max = d
#if a<b and a>c and a>d:
#    min = a
#elif b<a and b<c and b>d:
#    min = b
#elif c<a and c<b and c<d:
#    min = c
#elif d<a and d<c and d<c:
#    min = d
#print(min,max)

from random import randint

lst = [randint(-10, 10) for i in range(20)]
print(lst)

sum_negative = 0

for num in lst:
    if num < 0: sum_negative += num
print ("Sum negative item list: ", sum_negative)

sum_of_even = 0
for num in lst:
    if num % 2 == 0:
        sum_of_even += num
print("Sum of even item list:", sum_of_even)

sum_of_odd = 0
for num in lst:
    if num% 2 != 0:
        sum_of_odd += num
print("Sum of odd item list:", sum_of_odd)

# sum_elements_mult_3 = 0
# for i in range(len(lst)):
