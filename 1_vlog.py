"""
Big O Notation Lesson
====================

Big O notation describes how the runtime or memory usage of an algorithm
scales as the input size grows.

It helps us compare solutions without depending on the exact machine.

Common Big O classes:
- O(1)  -> Constant time
- O(log n) -> Logarithmic time
- O(n) -> Linear time
- O(n log n) -> Linearithmic time
- O(n^2) -> Quadratic time
- O(2^n) -> Exponential time

Examples below show how each idea can look in Python.
"""


def get_first(arr):
    """O(1): directly accesses the first element."""
    return arr[0]


def linear_search(arr, target):
    """O(n): checks each element until it finds the target."""
    for item in arr:
        if item == target:
            return True
    return False


def contains_duplicates(arr):
    """O(n^2): compares each item with every other item."""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


def binary_search(arr, target):
    """O(log n): repeatedly halves the search space."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    print("Big O Notation")
    print("--------------")
    print("\n1) O(1) example")
    numbers = [10, 20, 30, 40]
    print("First element:", get_first(numbers))

    print("\n2) O(n) example")
    print("Does 30 exist?", linear_search(numbers, 30))

    print("\n3) O(log n) example")
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13]
    print("Does 9 exist using binary search?", binary_search(sorted_numbers, 9))

    print("\n4) O(n^2) example")
    print("Contains duplicates?", contains_duplicates([1, 2, 3, 2]))

    print("\nKey idea:")
    print("As the input grows, the algorithm with the smaller Big O is usually better.")
    print("For example, O(log n) and O(1) are often faster than O(n^2) for large datasets.")