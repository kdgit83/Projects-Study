from dataclasses import dataclass, field

from Project_App_CoffeeMachine.oop_coffee_menu import CoffeeMenu
from Project_App_CoffeeMachine.oop_coffee_payment import CoffeePayment
from Project_App_CoffeeMachine.oop_coffee_resource import CoffeeResource


@dataclass
class CoffeeMachine:
    coffee_menu: CoffeeMenu = field(init=False, default_factory=CoffeeMenu)
    coffee_payment: CoffeePayment = field(init=False, default_factory=CoffeePayment)
    coffee_resource: CoffeeResource = field(init=False, default_factory=CoffeeResource)

    def is_resource_sufficient(self, order_ingredients: dict) -> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in order_ingredients:
            if order_ingredients[item] > self.coffee_resource.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink_name: str, order_ingredients: dict) -> None:
        """Deducts the required ingredients from the resources."""
        for item in order_ingredients:
            self.coffee_resource.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    while True:
        options = coffee_machine.coffee_menu.get_menu_items()
        user_input = input(f"What would you like? ({options}): ")
        if user_input == "off":
            print("Machine is now shutting down for maintenance.")
            break
        elif user_input == "report":
            coffee_machine.coffee_resource.resource_report()
            coffee_machine.coffee_payment.profit_report()
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
                coffee_machine.coffee_resource.resource_addition(coffee_ingredient, ingredient_quantity)
        elif user_input not in options:
            print("Invalid input. Please try again.")
            continue
        else:
            drink = coffee_machine.coffee_menu.get_drink_item(user_input)
            if (coffee_machine.is_resource_sufficient(drink["ingredients"]) and
                    coffee_machine.coffee_payment.make_payment(drink["cost"])):
                coffee_machine.make_coffee(user_input, drink["ingredients"])
