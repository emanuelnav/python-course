import random

def generatePassword():
    uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbs = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    length = int(input('choose a length for the password: '))
    characters = uppers + lowers + numbs + symbs
    password = []
    for i in range(length):
        random_char = random.choice(characters)
        password.append(random_char)
    return("".join(password))


def run():
    p = generatePassword()
    print('Your new password is: {}'.format(p))

if __name__ == '__main__':
    run()
