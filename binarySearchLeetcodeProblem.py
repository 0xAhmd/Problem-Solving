"""
Problem:
Given a sorted list of names and phone numbers, implement binary search to efficiently find the phone number associated with a specific name.

Time Complexity:
Binary search offers logarithmic time complexity (O(log n)), where 'n' is the number of elements in the sorted list. This efficiency allows for quick retrieval of phone numbers, especially in scenarios with large datasets.

Space Complexity:
The space complexity of binary search is constant (O(1)), as it uses only a few extra variables regardless of the size of the input data. This makes it memory-efficient and suitable for use in resource-constrained environments.
"""

def binary_search(phone_book, target_name):
    low = 0
    high = len(phone_book) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_name, phone_number = phone_book[mid]
        
        if mid_name == target_name:
            return phone_number
        elif mid_name < target_name:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

# Example usage:
phone_book = [
    ("Alice", "123-456-7890"),
    ("Bob", "234-567-8901"),
    ("Charlie", "345-678-9012"),
    ("David", "456-789-0123"),
    ("Emma", "567-890-1234")
]

target_name = "Ahmed"  # Corrected name
target_name2 = "Bob"

phone_number1 = binary_search(phone_book, target_name)  # Store result in phone_number1
phone_number2 = binary_search(phone_book, target_name2)  # Store result in phone_number2

if phone_number1:  # Check if phone_number1 is not None
    print(f"The phone number of {target_name} is {phone_number1}")
else:
    print(f"{target_name} is not found in the phone book.")

if phone_number2:  # Check if phone_number2 is not None
    print(f"The phone number of {target_name2} is {phone_number2}")
else:
    print(f"{target_name2} is not found in the phone book.")
