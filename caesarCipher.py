initial_text = input("Enter your text: ")
increment_number = int(input("Enter the increment number: "))  # Convert increment_number to an integer
loop_limit = len(initial_text)
caesar_text = ""
for i in range(loop_limit):
    char = initial_text[i]
    if char.isalpha():
        shift = increment_number
        if char.isupper():
            caesar_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            caesar_text += chr((ord(char) + shift - 97) % 26 + 97)
    else:
        caesar_text += char
print("Caesar Cipher Text:", caesar_text)
