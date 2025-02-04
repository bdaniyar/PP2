def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

# Example Usage
numbers = [1, 2, 2, 3, 3, 4, 5]
print("Unique elements:", unique_elements(numbers))
