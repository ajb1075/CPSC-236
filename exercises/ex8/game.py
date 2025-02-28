from random import randrange

def guess(guess: int, number: int) -> bool:
    if not 0 <= guess <= 100:
        '''Guess Out of Bounds'''
        print("Invalid Number!")
    elif guess != number:
        '''Show Hint if Guess is Not Correct'''
        print("Too High!" if guess > number else "Too Low!")
    else:
        '''If Guess is Correct'''
        return True
    return False

if __name__ == '__main__':
    number = randrange(0, 101)
    while not guess(int(input("Guess (Enter an Integer 1-100): ")), number):
        pass
    print("You Win!")
