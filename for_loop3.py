"""
for_loop3
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in nums:
    # add  one to each of the nums
    if i % 2 == 0:
        # if i modulus 2 or is equal to 0
        #  if i is and even number print it * 2
        print(i*2)

    if i % 2 != 0:
        print("odd ", i)
