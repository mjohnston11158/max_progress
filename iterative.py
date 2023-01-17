""""iterative"""



def factorial(number): 
    product = 1
    for i in range(number):
        product = product * (i+1)
    return product
print(factorial)