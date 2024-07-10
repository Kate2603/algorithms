### Просторова складність алгоритму — це кількість пам'яті, яку він використовує відносно розміру вхідних даних

# Просторова складність 𝑂(1)
def get_item_by_index(items, index):
    return items[index]

# Просторова складність O(n)
def reverse_list(items):
    return items[::-1]

# Просторова складність O(n2)
def generate_pairs(items):
    return [(items[i], items[j]) for i in range(len(items)) for j in range(i+1, len(items))]

items = [1, 2, 3, 4]
print(generate_pairs(items))



