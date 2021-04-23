"""
Hangman Game
"""

import random
import string
alpha = string.ascii_lowercase

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    s = set()
    for letter in lettersGuessed:
        if letter in secretWord:
            s.add(letter)
        else:
            continue
    if s == set(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word = word + letter
        else:
            word = word + '_ '

    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    let = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for c in alpha:
        if c not in lettersGuessed:
            let += c
    return''.join(let)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = chooseWord(wordlist).lower()
    lettersGuessed = []
    mistakesMade = 0

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('_____________')
            print("Congratulations, you won!")
            break
        else:
            print('_____________')
            print("You have", 8-mistakesMade, "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            i = input("Please guess a letter: ").lower()

            if i in secretWord and i not in lettersGuessed:
                lettersGuessed.append(i)
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            elif i in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            elif i not in secretWord:
                lettersGuessed.append(i)
                print("Oops! That letter is not in my word:", (getGuessedWord(secretWord, lettersGuessed)))
                mistakesMade += 1
        if 8 - mistakesMade == 0:
            print('_____________')
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break
        else:
            continue

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
