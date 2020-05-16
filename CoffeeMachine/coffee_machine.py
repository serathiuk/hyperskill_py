ESPRESSO_CODE = 1
ESPRESSO_WATER_NEEDS = 250
ESPRESSO_MILK_NEEDS = 0
ESPRESSO_COFFEE_NEEDS = 16
ESPRESSO_COST = 4

LATTE_CODE = 2
LATTE_WATER_NEEDS = 350
LATTE_MILK_NEEDS = 75
LATTE_COFFEE_NEEDS = 20
LATTE_COST = 7

CAPPUCCINO_CODE = 3
CAPPUCCINO_WATER_NEEDS = 200
CAPPUCCINO_MILK_NEEDS = 100
CAPPUCCINO_COFFEE_NEEDS = 12
CAPPUCCINO_COST = 6

water_stored = 400
milk_stored = 540
coffee_stored = 120
disposable_cups = 9
money = 550


def main():
    print_machine_report()

    action = input('Write action (buy, fill, take):')
    if action == 'buy':
        choose_buy()
    elif action == 'take':
        take_money()
    elif action == 'fill':
        fill_machine()

    print_machine_report()


def choose_buy():
    coffee_option = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))
    if coffee_option == ESPRESSO_CODE:
        buy_espresso()
    elif coffee_option == LATTE_CODE:
        buy_latte()
    elif coffee_option == CAPPUCCINO_CODE:
        buy_cappuccino()
    else:
        print('Invalid coffee option.')


def buy_espresso():
    return buy_coffee_by_recipe(ESPRESSO_WATER_NEEDS, ESPRESSO_MILK_NEEDS, ESPRESSO_COFFEE_NEEDS, ESPRESSO_COST)


def buy_latte():
    return buy_coffee_by_recipe(LATTE_WATER_NEEDS, LATTE_MILK_NEEDS, LATTE_COFFEE_NEEDS, LATTE_COST)


def buy_cappuccino():
    return buy_coffee_by_recipe(CAPPUCCINO_WATER_NEEDS, CAPPUCCINO_MILK_NEEDS, CAPPUCCINO_COFFEE_NEEDS, CAPPUCCINO_COST)


def buy_coffee_by_recipe(water_qty, milk_qty, coffee_qty, price):
    global water_stored, milk_stored, coffee_stored, disposable_cups, money
    water_stored -= water_qty
    milk_stored -= milk_qty
    coffee_stored -= coffee_qty
    disposable_cups -= 1
    money += price
    return True


def take_money():
    global money
    print('I gave you $'+str(money))
    money = 0


def print_machine_report():
    print()
    print('The coffee machine has:')
    print(water_stored, 'of water')
    print(milk_stored, 'of milk')
    print(coffee_stored, 'of coffee beans')
    print(disposable_cups, 'of disposable cups')
    print(money, 'of money')
    print()


def fill_machine():
    global water_stored, milk_stored, coffee_stored, disposable_cups
    water_qty = int(input('Write how many ml of water do you want to add:'))
    milk_qty = int(input('Write how many ml of milk do you want to add:'))
    coffee_qty = int(input('Write how many grams of coffee beans do you want to add:'))
    cups_qty = int(input('Write how many disposable cups of coffee do you want to add:'))
    water_stored += water_qty
    milk_stored += milk_qty
    coffee_stored += coffee_qty
    disposable_cups += cups_qty


main()
