from dataclasses import dataclass


@dataclass
class CoffeeResource:

    def __post_init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def resource_addition(self, ingredient_name: str, ingredient_amount: int) -> None:
        """Adds the supplied ingredient quantity to the given ingredient."""
        self.resources[ingredient_name] += ingredient_amount

    def resource_report(self) -> None:
        """Prints the current coffee resources and money profit."""
        for key, value in self.resources.items():
            if key != "coffee":
                print(f"{key}: {value}ml")
            else:
                print(f"{key}: {value}g")
