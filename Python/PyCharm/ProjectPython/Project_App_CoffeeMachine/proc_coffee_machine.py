from proc_coffee_menu import COFFEE_MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_addition(ingredient_name: str, ingredient_amount: int) -> None:
    """Adds the supplied ingredient quantity to the given ingredient."""
    resources[ingredient_name] += ingredient_amount


def resource_report(coffee_resources: dict, money_profit: int) -> None:
    """Prints the current coffee resources and money profit."""
    for key, value in coffee_resources.items():
        if key != "coffee":
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: {value}g")
    print(f"Money: ${money_profit}")


def is_resource_sufficient(order_ingredients: dict) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins(drink_name: str, drink_cost: float) -> float:
    """Returns the total calculated from coins inserted."""
    print(f"{drink_name} costs ${drink_cost}")
    print("Please insert coins.")
    total = 0.0
    total += int(input("how many quarters($0.25)?: ")) * 0.25
    total += int(input("how many dimes($0.10)?: ")) * 0.1
    total += int(input("how many nickles($0.05)?: ")) * 0.05
    total += int(input("how many pennies($0.01)?: ")) * 0.01
    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """Returns True when the payment is accepted, or False if money is insufficient."""
    global profit
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    elif money_received == drink_cost:
        print(f"Thank you for the exact drink price.")
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded ${money_received}.")
        return False


def make_coffee(drink_name: str, order_ingredients: dict) -> None:
    """Deducts the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if user_input == "off":
        print("Machine is now shutting down for maintenance.")
        break
    elif user_input == "report":
        resource_report(resources, profit)
    elif user_input == "add":
        while True:
            coffee_ingredient = input(f"Which ingredient you want to add? Water, Milk or Coffee: ").lower().strip()
            if coffee_ingredient.startswith('w'):
                coffee_ingredient = 'water'
            elif coffee_ingredient.startswith('m'):
                coffee_ingredient = 'milk'
            elif coffee_ingredient.startswith('c'):
                coffee_ingredient = 'coffee'
            else:
                break
            ingredient_quantity = int(input(f"How much {coffee_ingredient} you would like to add? "))
            resource_addition(coffee_ingredient, ingredient_quantity)
    elif user_input not in ["espresso", "latte", "cappuccino"]:
        print("Invalid input. Please try again.")
        continue
    else:
        drink = COFFEE_MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(user_input, drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
