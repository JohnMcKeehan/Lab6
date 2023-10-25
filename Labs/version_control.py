#John McKeehan

op = 0
original_password = None
encoded_password = None



def encoder(number):
    s = ""
    for i in number:
        s += str(int(i) + 3)
    return s

def decoder(number):
    s = ""
    for i in number:
        s += str(int(i) - 3)
    return s

def encoder(number):
    s = ""
    for i in number:
        s += str(int(i) - 3)
    return s
def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    op = int(input(f"Please enter an option: "))
    if op == 1:
        original_password = input(f'Please enter your password to encode:')
        if len(original_password) == 8:
            encoded_password = encoder(original_password)
            print('Your Password has been encoded and stored!')
        else:
            print("Error")
    if op == 2:
        print(f'The encoded password is {encoded_password}, and the original password is {original_password}')
    if op == 3:
        quit()

if __name__ == "__main__":
    main()