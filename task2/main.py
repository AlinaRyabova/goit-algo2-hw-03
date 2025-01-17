import os
from data_loading import load_data
from data_structures import add_item_to_tree, add_item_to_dict, range_query_tree, range_query_dict
from performance import measure_performance
from BTrees.OOBTree import OOBTree

def main():
    # Шлях до файлу
    data_file = "generated_items_data.csv"
    
    # Завантаження даних
    items = load_data(data_file)
    
    # Створення структур
    tree = OOBTree()
    dictionary = {}
    
    # Додавання даних
    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)
    
    # Визначення діапазону цін
    price_min = 100
    price_max = 400
    
    # Вимірювання продуктивності
    print("Вимірювання продуктивності...")
    time_tree = measure_performance(range_query_tree, tree, price_min, price_max, repetitions=100)
    time_dict = measure_performance(range_query_dict, dictionary, price_min, price_max, repetitions=100)

    
    # Результати
    print(f"Час виконання для OOBTree (100 запитів): {time_tree:.4f} секунд")
    print(f"Час виконання для dict (100 запитів): {time_dict:.4f} секунд")

if __name__ == "__main__":
    main()
