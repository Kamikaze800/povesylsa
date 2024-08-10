import random

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.objects import HANGMAN_PICS
from app.utils import drawHangman

router = Router()

@router.message(CommandStart())
async def main(message: Message):
    await drawHangman(missedLetters, correctLetters, secretWord, message)
    await message.answer('букву дай')


CATEGORY = 'Animals'
# WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()
WORDS = 'ANT BABOON'.split()
missedLetters = []  # List of incorrect letter guesses.
correctLetters = []  # List of correct letter guesses.
secretWord = random.choice(WORDS)  # The word the player must guess.
alreadyGuessed = []

@router.message()
async def game(message: Message):

    if len(message.text) != 1:
        await message.answer('одну букву')
        return



    global alreadyGuessed
    guess = message.text.upper()
    if guess in alreadyGuessed:
        await message.answer('Эта была, дай другую')
        return
    else:
        alreadyGuessed += guess

    if guess in secretWord:
        # Add the correct guess to correctLetters:
        correctLetters.append(guess)

        # Check if the player has won:
        foundAllLetters = True  # Start off assuming they've won.
        for secretWordLetter in secretWord:
            if secretWordLetter not in correctLetters:
                # There's a letter in the secret word that isn't
                # yet in correctLetters, so the player hasn't won:
                foundAllLetters = False

        await drawHangman(missedLetters, correctLetters, secretWord, message)

        if foundAllLetters:
            await message.answer(f'Yes! The secret word is: {secretWord}')
            await message.answer('You have won!')




    elif len(missedLetters) == len(HANGMAN_PICS) - 1:
        missedLetters.append(guess)
        await message.answer('You have run out of guesses!')
        await message.answer('The word was "{}"'.format(secretWord))
        return
    else:
        missedLetters.append(guess)
        await drawHangman(missedLetters, correctLetters, secretWord, message)
        await message.answer('букву гони')
