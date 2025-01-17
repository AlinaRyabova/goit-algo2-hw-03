def add_item_to_tree(tree, item):
    """Додавання товару до OOBTree."""
    tree[item["ID"]] = item

def add_item_to_dict(dictionary, item):
    """Додавання товару до словника."""
    dictionary[item["ID"]] = item

def range_query_tree(tree, min_price, max_price):
    """Діапазонний запит у OOBTree."""
    return [
        item for key, item in tree.items()
        if min_price <= item["Price"] <= max_price
    ]

def range_query_dict(dictionary, min_price, max_price):
    """Діапазонний запит у словнику."""
    return [
        item for key, item in dictionary.items()
        if min_price <= item["Price"] <= max_price
    ]
