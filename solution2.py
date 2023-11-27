def check_positives(a, b, c):
    # Initialize a counter for positive integers
    positive_count = 0
     # Check if each integer is positive and increment the counter 
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
        # Return True if exactly two integers are positive
    return positive_count == 2

print(check_positives(8, 4, -1))  # Output: True
print(check_positives(-7, 5, 3))  # Output: True
print(check_positives(-5, 3, 0))  # Output: False
print(check_positives(4, 2, 10))  # Output: False