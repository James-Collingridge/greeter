name = input("Enter your name: ")
sanitized_name = name[0].upper() + name[1:].lower()
vowel = ['A', 'E', 'I', 'O', 'U']

print("Hello " + sanitized_name + "!")
if sanitized_name[0] in vowel:
    print("Your name begins with a vowel.")
else:
    print("Your name does not begin with a vowel.")
