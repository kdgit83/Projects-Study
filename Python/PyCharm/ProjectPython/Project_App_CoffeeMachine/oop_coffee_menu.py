from dataclasses import dataclass
from proc_coffee_menu import COFFEE_MENU


@dataclass
class CoffeeMenu:
    menu_details = COFFEE_MENU

    def get_menu_items(self) -> str:
        """Returns all the names of the available menu items"""
        items = ""
        for item in self.menu_details:
            items += f"{item} / "
        items = items.rstrip(' / ')
        return items

    def get_drink_item(self, drink_name: str) -> dict:
        """Returns the drink details."""
        for item in self.menu_details:
            if item == drink_name:
                return self.menu_details[item]

    def get_item_ingredients(self, item_name: str) -> dict:
        """Returns ingredients of the given item name"""
        ingredient_dict = {}
        for item in self.menu_details:
            if item == item_name:
                ingredient_dict.update(self.menu_details[item_name]['ingredients'])
        return ingredient_dict

    def get_item_cost(self, item_name: str) -> float:
        """Returns cost of the given item name"""
        item_cost = 0
        for item in self.menu_details:
            if item == item_name:
                item_cost += self.menu_details[item_name]['cost']
        return item_cost
