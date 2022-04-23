MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money in machine": 0,
}


# Function declarations ----------------------------------------------------------------------------


def resource_checker(beverage_type):
    """ Checks if the resources in the coffee machine is enough to dispense coffee"""
    for item in MENU[beverage_type]["ingredients"]:
        if resources[item] < MENU[beverage_type]["ingredients"][item]:
            resource_sufficient = False
            return resource_sufficient
        else:
            resource_sufficient = True
    return resource_sufficient


def total_money_calculator(q, d, n, p):
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    return round(total, 2)


def dispense_coffee(menu, user_choice, total_coins_inserted):
    """ checks if money inserted is enough to dispense coffee and dispenses coffee """
    if user_choice == "espresso" and menu[user_choice]["cost"] <= total_coins_inserted:
        print(f"Here is your {user_choice}!")
    elif user_choice == "latte" and menu[user_choice]["cost"] <= total_coins_inserted:
        print(f"Here is your {user_choice}!")
    elif user_choice == "cappuccino" and menu[user_choice]["cost"] <= total_coins_inserted:
        print(f"Here is your {user_choice}!")
    else:
        print("You haven't inserted enough Money!")
        print(f"Money returned : {total_coins_inserted}")
        return False
    change = round(total_coins_inserted - menu[user_choice]["cost"], 2)
    print(f"Here is your change {change}")
    return True


def resource_deductor(beverage_type):
    """Once coffee is dispensed - resources are deducted from the machine and money is added to the machine"""
    for item in MENU[beverage_type]["ingredients"]:
        resources[item] = resources[item] - MENU[beverage_type]["ingredients"][item]
    resources["Money in machine"] += MENU[beverage_type]["cost"]
    return resources

# Function declarations ends ---------------------------------------------------------------------------------


make_coffee = True

while make_coffee:
    choice = input("What would you like to have ? espresso/latte/cappuccino : ").lower()
    if choice == "report":
        print(resources)
    else:
        print("Please Insert coins : ")
        quarter = int(input("Insert Quarters : "))
        dime = int(input("Insert dimes : "))
        nickle = int(input("Insert nickles : "))
        penny = int(input("Insert pennies : "))

        coin_total = total_money_calculator(quarter, dime, nickle, penny)

        if resource_checker(choice):
            print("The coffee machine has sufficient resources :)")
            if dispense_coffee(MENU, choice, coin_total):
                resources = resource_deductor(choice)
        else:
            print("The machine does not have ingredients to make coffee :( - please refill the machine...")
            print(f"Your money has been refunded- {coin_total}")
            make_coffee = False



































