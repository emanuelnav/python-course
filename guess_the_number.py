from random import randint

def run():
    print('A game where you have to guess a number between 1 to 100')
    number = int(input('Choose a number between 1 to 100: '))
    randomNumber = randint(1, 100)
    while(number != randomNumber):
        if number < randomNumber:
            print('Choose a bigger number')
        else:
            print('Choose a smaller number')
        number = int(input('Choose another number: '))
    print('You Win!')

if __name__ == '__main__':
    run()
