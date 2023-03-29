"""
my_first_algo
a program that iterated between integers 1-50
multiples of 3 print fizz
for multiples of 5 print buzz
for multiples of 5 and 3 print fizzbuzz

"""
for i in range(25):
    if i % 3 == 0:
        print("FiZZ!")
    elif i % 5 == 0:
        print("BuZZ!")
    elif i % 5 or 3 == 0:
        print("FiZZBuZZ!")
