# print report
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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

def report():
    for i,v in resources.items():
        if i == 'Coffee':
            print(f'{i}: {v}g')
        elif i == 'Money':
            print(f'{i}: ${v}')
        else:
            print(f'{i}: {v}ml')
    
def create_order(drink):
    flag = False
    dict = (MENU.get(drink)).get('ingredients')
    water = dict['water']
    milk = dict['milk']
    coffee = dict['coffee']
    if water >= resources['Water']:
        print('Sorry there is not enough water.')
        flag = True
    if milk >= resources['Milk']:
        print('Sorry there is not enough milk.')
        flag = True
    if coffee >= resources['Coffee']:
        print('Sorry there is not enough coffee.')
        flag = True
    if not flag:
        cost = (MENU.get(drink))['cost']
        finalize_transaction(cost,water,milk,coffee)
        

def finalize_transaction(cost,water,milk,coffee):
    print('Please Insert Coins: ')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    cash = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies *0.01)
    if cash < cost:
        print("Sorry that's not enough money. Money refunded.")
    else: 
        resources['Money'] += cost
        change_inv(cash-cost,water,milk,coffee)
    
def change_inv(change,water,milk,coffee):
    if change != 0:
        print(f'Here is ${round(change,2)} dollars in change.')
    #no need global to change dictionaries
    resources['Water'] -= water
    resources['Milk'] -= milk
    resources['Coffee'] -= coffee

def main():
    while True:
        #unseen options : off to exit loop, report to get report
        C1 = input("What would you like? (espresso/latte/cappuccino): ").lower()    
        if C1 == 'off':
            break
        if C1 == 'report':
            report()
        else:
            create_order(C1)
    
main()