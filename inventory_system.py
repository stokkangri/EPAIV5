import copy
from typing import Any

def normalize_category(category: str) -> str:
    """Normalize category name to capitalize the first letter and lowercase the rest."""
    return category.capitalize()

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    inventory: dict[str, dict[str, dict[str, Any]]] = {}

    # Using direct addition
    inventory[normalize_category("Electronics")] = {
        "Laptop": {"name": "Laptop", "price": 1000, "quantity": 5},
        "Smartphone": {"name": "Smartphone", "price": 600, "quantity": 30}
    }

    # Using dictionary comprehension
    new_electronics = {f"Cool Gadget {i}": {"name": f"Cool Gadget {i}", "price": 50 + i * 10, "quantity": 5} for i in range(1, 4)}
    inventory[normalize_category("Electronics")].update(new_electronics)

    # Using dict() constructor
    inventory[normalize_category("Groceries")] = dict(
        Fresh_Apples={"name": "Fresh Apples", "price": 1.5, "quantity": 100},
        Organic_Milk={"name": "Organic Milk", "price": 3, "quantity": 50},
        Yellow_Bananas={"name": "Yellow Bananas", "price": 0.5, "quantity": 150},
        Whole_Wheat_Bread={"name": "Whole Wheat Bread", "price": 2, "quantity": 30}
    )

    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    normalized_category = normalize_category(category)
    if normalized_category in inventory and item_name in inventory[normalized_category]:
        inventory[normalized_category][item_name].update(update_info)
    else:
        print(f"Item {item_name} not found in category {category}")

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    merged = copy.deepcopy(inv1)
    for category, itemlist in inv2.items():
        normalized_category = normalize_category(category)
        if normalized_category not in merged:
            merged[normalized_category] = itemlist
        else:
            #print ("Item is found in category - counts ", normalized_category, itemlist)
            for item, details in itemlist.items():
                if item in merged[normalized_category]:
                    merged[normalized_category][item]['price'] = details['price']
                    merged[normalized_category][item]['quantity'] += details['quantity']
                else:
                    merged[normalized_category][item] = details
    return merged

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    normalized_category = normalize_category(category)
    return inventory.get(normalized_category, {})

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    all_items = [item for category in inventory.values() for item in category.values()]
    return max(all_items, key=lambda x: x['price'])

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category, itemlist in inventory.items():
        for  item, details in itemlist.items():
            if item_name == item and details['quantity'] > 0:
                return details
    return None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return list(inventory.keys())

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    return [item for category in inventory.values() for item in category.values()]

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return [(category, item_name) for category, items in inventory.items() for item_name in items]

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    if deep:
        return copy.deepcopy(inventory)
    else:
        return copy.copy(inventory)
