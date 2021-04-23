"""
Removing letters from a hand (you implement this)
The player starts with a hand, a set of letters.
As the player spells out words, letters from this
set are used up. For example, the player could
start out with the following hand: a, q, l, m, u, i, l.
The player could choose to spell the word quail .
This would leave the following letters in the
player's hand: l, m. Your task is to implement the
function updateHand, which takes in two inputs -
a hand and a word (string). updateHand uses letters
from the hand to spell the word, and then returns a
copy of the hand, containing only the letters remaining.

Implement the updateHand function. Make sure this
function has no side effects: i.e., it must not mutate
the hand passed in. Before pasting your function definition
here, be sure you've passed the appropriate tests in test_ps4a.py
"""


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    updated = hand.copy()
    wordlen = 0

    # remove letters used in word
    for letter in updated:
        if letter in word:
            updated[letter] = updated.get(letter, 0) - word.count(letter)
            wordlen += word.count(letter)

    if wordlen == len(word):
        hand = updated

    return hand