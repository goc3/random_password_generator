import secrets
import random

# characters used in the random passwords
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spec_char = ['!', '#', '$', '%', '&', '*', '+', '-']
spec_char2 = [":", ";", "<", "=", ">", "?", "@"]

# function to generate random password
def gen_r_pass():
    new_pass = secrets.token_hex(8)
    spec_char_r = random.choice(spec_char)
    spec_char2_r = random.choice(spec_char2)
    chr_r = random.choice(alphabet)
    r_pass = press + chr_r + spec_char_r + new_pass + spec_char2_r + chr_r
    return r_pass

while True:
    main = True
    while main:
        press = input('Enter a phrase to generate your random password: ')
        press_spc_check = " " in press
        if press_spc_check is True:
            print('Empty spaces are not allowed. Please try again.')
            break
        press_empty_check = len(press)
        if press_empty_check == 0:
            print('Please enter a phrase.')
            break
        if press.isdigit():
            press = str(press)
            if len(press) > 5:
                print('You can only enter up to five characters.')
                break
            else:
                new_rand_pass = print('Your new random password is: ' + gen_r_pass())                
                main = False
        else:
            if len(press) > 5:
                print('You can only enter up to five characters.')
                break
            else:
                new_rand_pass = print('Your new random password is: ' + gen_r_pass())