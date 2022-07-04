MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


water=300
milk=200
coffee=100
money=0
def check_resourses_espresso():
    global water
    global milk
    global coffee
    if water <= 50 and coffee <=18:
        return True
    else:
        return False

def check_resourses_latte():
    global water
    global milk
    global coffee
    if water <=200  and coffee <=24 and milk > 150:
        return True
    else:
        return False

def check_resourses_cappuccino():
    global water
    global milk
    global coffee
    if water <=250  and coffee <=24 and milk > 100:
        return True
    else:
        return False








def machine():
    print(MENU)

    global water
    global milk
    global coffee
    global money
    game =True
    while game == True:
        ask=input("What would you like?(espresso/latte/cappuccino):")
        if ask == "espresso":
            if check_resourses_espresso:
                water -= 50
                coffee -=18
                pay=int(input("please enter coins"))
                if pay < 10:

                    print("money insufficent.money refunded")
                else:
                    money = money + pay
                    print("here is your espresso enjoy!")
                    machine()
            else:
                print("sorry we dont have enough resources")

        elif ask == "latte":
            if check_resourses_espresso:
                water -= 200
                coffee -= 24
                milk -= 150
                pay = int(input("please enter coins"))
                if pay <= 25:

                    print("money insufficent.money refunded")
                else:
                    money = money + pay
                    print("here is your latte enjoy!")
                    machine()
            else:
                print("sorry we dont have enough resources")

        elif ask == "cappuccino":
            if check_resourses_cappuccino():
                water -= 250
                coffee -= 24
                milk -= 100
                pay = int(input("please enter coins"))
                if pay <= 50:

                    print("money insufficent.money refunded")
                else:
                    money = money + pay
                    print("here is your latte enjoy!")
                    game()
            else:
                print("sorry we dont have enough resources")
        elif ask == "report":
            print("water:",water)
            print("coffee:",coffee)
            print("milk:",milk)
            print("money:" ,money)
            machine()
        else:
            game=False

machine()









