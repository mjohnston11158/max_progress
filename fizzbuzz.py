"""
my_first_algo
a program that iterated between integers 1-50
multiples of 3 print fizz
for multiples of 5 print buzz
for multiples of 5 and 3 print fizzbuzz

"""


for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz ", i)

    elif i % 3 == 0:
        print("fizz ", i)

    elif i % 5 == 0:
        print("buzz ", i)
