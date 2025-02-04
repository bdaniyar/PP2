def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]

# Example Usage
numbers = [10, 15, 23, 28, 35, 39, 41, 53, 61]
print("Prime numbers:", filter_prime(numbers))
