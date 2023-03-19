from typing import NamedTuple, List


class Item(NamedTuple):
    name: str
    weight: int
    value: float


def knapsack(items: List[Item], max_capacity: int) -> List[Item]:
    # Eine Tabelle für dynamische Programmierung aufbauen
    table: List[List[float]] = [[0.0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]
    for i, item in enumerate(items):
        for capacity in range(1, max_capacity + 1):
            previous_items_value: float = table[i][capacity]
            if capacity >= item.weight: # Gegenstand passt in Rucksack
                value_freeing_weight_for_item: float = table[i][capacity - item.weight]
                # Nur nehmen, wenn wertvoller als voriger Gegenstand
                table[i + 1][capacity] = max(value_freeing_weight_for_item + item.value, previous_items_value)
            else: # Kein Platz für diesen Gegenstand
                table[i + 1][capacity] = previous_items_value
    # Lösung aus der Tabelle heraussuchen
    solution: List[Item] = []
    capacity = max_capacity
    for i in range(len(items), 0, -1): # Rückwärts arbeiten
        # Wurde dieser Gegenstand verwendet?
        if table[i - 1][capacity] != table[i][capacity]:
            solution.append(items[i - 1])
            # Wenn dieser Gegenstand verwendet wurde, sein Gewicht abziehen
            capacity -= items[i - 1].weight
    return solution


if __name__ == "__main__":
    items: List[Item] = [Item("Fernseher", 50, 500),
                         Item("Kerzenhalter", 2, 300),
                         Item("Stereoanlage", 35, 400),
                         Item("Laptop", 3, 1000),
                         Item("Essen", 15, 50),
                         Item("Kleidung", 20, 800),
                         Item("Schmuck", 1, 4000),
                         Item("Bücher", 100, 300),
                         Item("Drucker", 18, 30),
                         Item("Kühlschrank", 200, 700),
                         Item("Gemälde", 10, 1000)]
    print(knapsack(items, 75))


