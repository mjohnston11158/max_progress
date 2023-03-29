#Let's start a coffee shop together!!  
#We're goin to build a coffee shop using some new Python programming concepts!!

# Let's build a robot barista!!


print("\n\nHello, welcome to Niahs Cafe")

name = input("What is your name? ")
if name == "Daddy".lower():
        print("kisses\n\n")


Diamond_Chocolate = "Diamond Chocolate"



Erupted_Volcano = "Erupted Volcano"


Robot_Mansion = "Robot Mansion"


greeting = "Hi, "

pitch = "What's the flavor? "

menu =  "\n\n     MENU    \n Diamond Chocolate Coffee $40.55\n Erupted Volcano Coffee $1million\n Robot Mansion Coffee $99.99\n\n"





order = input( greeting + name + "!\n" + menu + "\n" + pitch  + "\n")
if order == Diamond_Chocolate.lower():
        quantity = int(input("how many you want?"))
        price = 40.55
        total = quantity * price
        outro = "that will be $" + str(total) + " plus tax"
        if quantity > 1:
                print(str(quantity) + " Diamond Chocolate Coffees Coming right up!\n"+ outro)
        else:
                print( "\nOne Diamond Chocolate Coffee Coming right up!\n" + outro)

elif order == Erupted_Volcano.lower():
        quantity = int(input("how many you want?"))
        price = 1000000
        total = quantity * price
        outro = "that will be $" + str(total) + " plus tax"
        if quantity > 1:
                print(str(quantity) + " Erupted Volcano Coffees Coming right up!\n" + outro)
        else:
                print( "\nOne Erutpted Volcano Coffee COming right up!\n" + outro)        

elif order == Robot_Mansion.lower():
        quantity = int(input("how many you want?"))
        price = 90.99
        total = quantity * price
        outro = "that will be $" + str(total) + " plus tax"
        if quantity > 1:
                print(str(quantity) + " Robot Mansion Coffees Coming right up!\n" + outro)
        else:
                print( "\nOne Robot Mansion Coffee COming right up!\n" + outro)












        

