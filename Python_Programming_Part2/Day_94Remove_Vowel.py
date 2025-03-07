"""
Remove Vowels from given string
"""
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result

# Example usage
input_string = "Hello, World!"
output_string = remove_vowels(input_string)
print(output_string)  # Output: "Hll, Wrld!"