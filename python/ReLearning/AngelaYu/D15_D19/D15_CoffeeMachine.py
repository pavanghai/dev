MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def show_resource():
    return (f"water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
          f"coffee: {resources['coffee']}g\nMoney: ${resources['money']}")      

def make_coffee(menu_item):
    resources['water'] -= menu_item['ingredients']['water']
    resources['milk'] -= menu_item['ingredients']['milk']
    resources['coffee'] -= menu_item['ingredients']['coffee']
    resources['money'] += menu_item['cost']


def process_coins():
    print("Please insert coins.")
    qrarters = int(input("How many quarters?: ") or "0")
    dimes = int(input("How many dimes?: ") or "0")
    nickles = int(input("How many nickles?: ") or "0")
    pennies = int(input("How many pennies?: ") or "0")
    total_amount = (qrarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    return total_amount


def check_resource(menu_item):
    if MENU[menu_item]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
    elif MENU[menu_item]['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk.")
    elif MENU[menu_item]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
    else:
        user_paid = process_coins()
        if user_paid > MENU[menu_item]['cost']:
            change = user_paid - MENU[menu_item]['cost']
            print(f"Here is ${round(change,2)} in change.")
            print(f"Here is your {menu_item} (coffee symbol) Enjoy!")
            make_coffee(MENU[menu_item])
        elif user_paid < MENU[menu_item]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is your {menu_item} (coffee symbol) Enjoy!")
            make_coffee(MENU[menu_item])
            
machine_status = "on"
user_choice_selection = ("espresso", "latte", "cappuccino", "report", "off")
while machine_status == "on":
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice not in user_choice_selection:
        print("Invalid selection")
        continue
    if user_choice == "off":
        machine_status = "off"
    if user_choice == "report":
        print(show_resource())
    if user_choice in ("espresso", "latte", "cappuccino"):
        check_resource(user_choice)