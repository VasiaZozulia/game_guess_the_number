"""
Умова задачі:
Генерація числа:
     Програма випадковим чином обирає ціле число у заданому діапазоні (наприклад, від 1 до 100).
Кількість спроб:
     Гравцю надається обмежена кількість спроб (наприклад, 7), щоб вгадати це число.
Введення гравця:
     Користувач вводить свої здогадки через консоль.
Підказки:
     Після кожної спроби програма виводить підказку:
          Якщо введене число менше загаданого — повідомляється "Занадто маленьке".
          Якщо більше — "Занадто велике".
          Якщо вгадано точно — виводиться привітання з перемогою.
Завершення гри:
          Якщо користувач вичерпав усі спроби, програма виводить повідомлення про поразку і розкриває загаданe число.
"""
import random

# Define the range within which the number will be guessed
guess_range = (1, 100)

# Set the maximum number of attempts the user has to guess the number
tries = 7

# Dictionary containing hints for the user's guesses
tips = {
    'small': 'Your number is too small',
    'big': 'Your number is too hight',
    'win' : 'Congratulations, you won the game!',
    'loss' : 'Unfortunately, you lost the game. All your attempts were unsuccessful.',
    'input_guess_message' : 'Enter your assumption: ',
    'range_error' : 'The range within which the number will be guessed is incorrect. The first value should be smaller than the second value.',
    'input_number_error' : 'Please enter the whole number!',
}

# The result of the game
game_result = False

# Checking if the guess range is within the correct bounds.
try:
    # Randomly select a number between the specified range
    random_number = random.randint(guess_range[0], guess_range[1])

    print ("Welcome to the game 'Guess the Number.'")
    print (f"I’ve picked a number between {guess_range[0]} and {guess_range[1]}. You have {tries} tries to guess it. Let's play!")

    # Start the game
    while tries > 0:
        try:
            guess = int(input(tips['input_guess_message']))
        except ValueError:
            print (tips['input_number_error'])
            continue

        # Checking if the user's number is within the correct bounds.
        if guess < guess_range[0] or guess > guess_range[1]:
            print (f"The number should be between {guess_range[0]} and {guess_range[1]}")
            continue

        # Checking if the user's input number equal random number
        if guess == random_number:
            print (f"{tips['win']}. The number was {random_number}.")
            game_result = True
            break
        elif guess < random_number:
            print (f"{tips['small']}.")
        else:
            print (f"{tips['big']}.")

        # User attempts decrease each time they try to guess the number.
        tries -= 1
        print (f"{tries} tries left! Try again!")

    if not game_result:
        print (f"{tips['loss']} The number was {random_number}.")

except ValueError:
    print (tips['range_error'])
