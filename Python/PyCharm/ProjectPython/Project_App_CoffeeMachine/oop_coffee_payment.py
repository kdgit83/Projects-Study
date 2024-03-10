from dataclasses import dataclass


@dataclass
class CoffeePayment:
    CURRENCY: str = "$"
    COIN_VALUES = {
        "quarters($0.25)": 0.25,
        "dimes($0.10)": 0.10,
        "nickles($0.05)": 0.05,
        "pennies($0.01)": 0.01
    }
    money_received = 0.0

    def __post_init__(self):
        self.profit = 0.0
        self.money_received = 0.0

    def profit_report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted or False if insufficient."""
        self.process_coins()
        if self.money_received > cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0.0
            return True
        elif self.money_received == cost:
            print(f"Thank you for the exact drink price.")
            self.profit += cost
            self.money_received = 0.0
            return True
        else:
            print(f"Sorry that's not enough money. Money refunded ${round(self.money_received, 2)}.")
            self.money_received = 0.0
            return False
