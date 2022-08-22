alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, dir_input):
    cipher_text = ""
    if dir_input == "encode":
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text = cipher_text + new_letter
        print(f"The encode text is {cipher_text}")
    elif dir_input == "decode":
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text = cipher_text + new_letter
        print(f"The encode text is {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(plain_text=text, shift_amount=shift, dir_input=direction)
    else:
        print("Wrong Input")
    result = input("Type 'yes' if you want to go again, Otherwise type 'no': \n")
    if result == 'no':
        should_continue = False
        print("Goodbye")


