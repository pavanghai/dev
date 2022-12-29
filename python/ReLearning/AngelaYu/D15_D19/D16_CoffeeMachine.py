from D16_menu import Menu, MenuItem
from D16_coffee_maker import CoffeeMaker
from D16_money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) and \
                money_machine.make_payment(menu.find_drink(choice).cost):
            coffee_maker.make_coffee(menu.find_drink(choice))