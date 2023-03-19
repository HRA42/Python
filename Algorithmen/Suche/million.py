from random import randint
import timeit
from typing import List


def binary_contains(index: int = [], target: int = 0) -> bool:
    low: int = 0
    high: int = len(index) - 1
    while low <= high:  # solange es noch einen Suchraum gibt
        mid: int = (low + high) // 2
        if index[mid] < target:
            low = mid + 1
        elif index[mid] > target:
            high = mid - 1
        else:
            return True
    return False


def linear_contains(index: int = [], target: int = 0) -> bool:
    for i in index:
        if i == target:
            return True
    return False


def random_numer(low: int = 0, high: int = 1000000) -> int:
    return randint(low, high)


def create_index(min: int, max: int) -> List[int]:
    index: int = []
    for i in range(min, max):
        index.append(i)
    return index


if __name__ == "__main__":
    index: int = create_index(0, 1000000)
    result_bc = timeit.repeat('binary_contains(index, random_numer())', globals=globals(), number=100)
    result_lc = timeit.repeat('linear_contains(index, random_numer())', globals=globals(), number=100)
    print("Binary search duration: {}".format(min(result_bc)))
    print("Linear search duration: {}".format(min(result_lc)))
    print("Binary search is " + str(round((min(result_lc) / min(result_bc)))) + " times faster than linear search")
