from app.objects import HANGMAN_PICS
from aiogram.types import Message


async def drawHangman(missedLetters, correctLetters, secretWord, message: Message):
    vyvod = []
    """Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word."""
    vyvod.append(HANGMAN_PICS[len(missedLetters)])

    vyvod.append('')

    # Show the incorrectly guessed letters:
    vyvod.append('Missed letters: ')
    for letter in missedLetters:
        vyvod.append(letter)
    if len(missedLetters) == 0:
        vyvod.append('No missed letters yet.')
    vyvod.append('')

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter:
    vyvod.append(' '.join(blanks))

    await message.answer('\n'.join(vyvod))


