"""ANIMAL_CALCULATOR"""


a = int(input("what was your income? $")) 


b = int(input("what is ur overhead? $"))  



if a > b:
    print('$',a-b,"profit")
    print("we ARE animals!!!")
    

else:
    print('$',a-b,"you took a loss!\nback to the lab!")
    
    

def balance(balance):
    balance = a-b
    return balance 