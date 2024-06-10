from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


def main():
    while True:
        C1 = input(f'What would you like? ({my_menu.get_items()}): ').lower()
        if C1 == 'off':
            break
        elif C1 == 'report':
            print(my_money_machine.report())
        else:
            drink = my_menu.find_drink(C1)
            flag = my_coffee_maker.is_resource_sufficient(drink)
            if flag:    
                cost = float(my_menu.find_drink(C1).cost)
                accepted = my_money_machine.make_payment(cost)
                if accepted:
                    my_coffee_maker.make_coffee(drink)
main()