def letter_occurrences(word: str) -> dict:
    """
    Returns a dictionary with the number of 
    occurrences of each letter in a word
    """
    letters = {}

    for letter in word:
        if letters.get(letter) == None:
            letters[letter] = 0
        letters[letter] += 1
    return letters

def is_anagram(word: str, potential_anagram: str) -> bool:
    """
    Returns whether two words are anagrams
    - Case insensitive
    - Non-alphabetic characters are ignored
    """
    word = remove_non_alphabetic_characters(word.upper())
    potential_anagram = remove_non_alphabetic_characters(potential_anagram.upper())

    if (not len(word) == len(potential_anagram)):
        return False

    for letter in word:
        pos = potential_anagram.find(letter)
        if pos == 0:
            potential_anagram = potential_anagram[1:]
        elif pos > 0:
            potential_anagram = potential_anagram[0:pos-1] + potential_anagram[pos+1:]

    return len(potential_anagram) == 0

def remove_non_alphabetic_characters(word: str) -> str:
    alphabetic_word = ''
    for letter in word:
        if letter.isalpha():
            alphabetic_word += letter
    return alphabetic_word
