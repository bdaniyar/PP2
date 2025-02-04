def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

# Example Usage
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
