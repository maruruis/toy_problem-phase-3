def check_highest_consonant_value(string):
    # Define vowels and create a dictionary to map consonants to their va
    vowels = "aeiou"
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

    max_value = 0
    current_value = 0
     # Iterate through each character in the input string
    for char in string:
        # Check if the character is not a vowel 
        if char not in vowels:
            current_value += consonant_values.get(char, 0)
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    # Check the last substring if the word ends with a consonant
    max_value = max(max_value, current_value)

    return max_value


result_zodiacs = check_highest_consonant_value("zodiacs")
result_strength = check_highest_consonant_value("strength")

print(" zodiacs:", result_zodiacs)
print("strength:", result_strength)
