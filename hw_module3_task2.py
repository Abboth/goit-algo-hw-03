#task № 2 in first homework

import random
min_val = 1
max_val = 1000
quantity_of_val = random.randint(min_val, max_val)

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    """
    наполняем множество уникальными значениями случайно сгенерированных чисел
    в промежутке от min_val до max_val
    количество получаемых значений = случайному значнию между min_val и max_val
    """
    random_value_set = set()
    if min >0 and max <=1000:
        while True:
            random_value_set.add(random.randint(min, max))
            if quantity == len(random_value_set):
                break

    return sorted(list(random_value_set))

print(get_numbers_ticket(min_val, max_val, quantity_of_val))