import heapq

def heap_sort(iterable, descending=False):
    # Визначаємо, який знак використовувати залежно від порядку сортування
    sign = -1 if descending else 1

		# Створюємо купу, використовуючи заданий порядок сортування
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
    return [sign * heapq.heappop(h) for _ in range(len(h))]

# Приклади використання функції
arr = [12, 11, 13, 5, 6, 7]
# Сортування за зростанням (за замовчуванням)
sorted_arr_asc = heap_sort(arr)
print("Відсортований масив (за зростанням):", sorted_arr_asc)
# Сортування за спаданням
sorted_arr_desc = heap_sort(arr, descending=True)
print("Відсортований масив (за спаданням):", sorted_arr_desc)
