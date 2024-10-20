
user_input = input("Enter a single character: ")

if len(user_input) == 1:
    ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is {ascii_value}.")
else:
    print("Please enter only one character.")
