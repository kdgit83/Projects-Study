import string
from art import logo

print(logo)
alphabets = list(string.ascii_lowercase)
alpha_count = len(alphabets)


def caeser(start_text: str, shift_amount: int, cipher_direction: str) -> None:
    end_text = ""
    for char in start_text:
        if char not in alphabets:
            end_text += char
        else:
            position = alphabets.index(char)
            if cipher_direction == "d" or cipher_direction == "decode":
                cipher_direction = "decode"
                if (position - shift_amount) >= 0:
                    new_position = position - shift_amount
                    new_letter = alphabets[new_position]
                    end_text += new_letter
                elif (position - shift_amount) < 0:
                    new_position = position - shift_amount + alpha_count
                    new_letter = alphabets[new_position]
                    end_text += new_letter
            elif cipher_direction == "e" or cipher_direction == "encode":
                cipher_direction = "encode"
                if (position + shift_amount) <= alpha_count - 1:
                    new_position = position + shift_amount
                    new_letter = alphabets[new_position]
                    end_text += new_letter
                elif (position + shift_amount) > alpha_count - 1:
                    new_position = position + shift_amount - alpha_count
                    new_letter = alphabets[new_position]
                    end_text += new_letter
    print(f"The {cipher_direction}d text is: {end_text}")


while True:
    direction = input("Type 'e' or 'encode' to Encrypt, type 'd' or 'decode' to Decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number, a positive integer number:\n"))
    shift = shift % 26
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye!!")
        break
