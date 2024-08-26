import pytest
from app.words import letter_occurrences, is_anagram

@pytest.mark.parametrize('word,expected', [
    ('', {}),
    ('a', {'a': 1}),
    ('ab', {'a': 1, 'b': 1}),
    ('abcdefghijklmnopqrstuvwxyz', {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}),
    ('Hello', {'H': 1, 'e': 1, 'l': 2, 'o': 1}),
    ('ZZZ', {'Z': 3}),
    ('aZZZ', {'a': 1, 'Z': 3}),
    ('Hello there', {'H': 1, 'e': 3, 'l': 2, 'o': 1, ' ': 1, 't': 1, 'h': 1, 'r': 1})
])
def test_letter_occurrences(word, expected):
    assert letter_occurrences(word) == expected

@pytest.mark.parametrize('word,anagram_succeeds', [
    ('elbow', 'below'),
    ('vase', 'save'),
    ('', ''),
    ('a', 'a'),
    ('', '8'),
    ('a gentleman', 'elegant man'),
    ('William Shakespeare', 'I\'ll make a wise phrase')
])
def test_is_anagram_succeeds(word, anagram_succeeds):
    assert is_anagram(word, anagram_succeeds)

@pytest.mark.parametrize('word,anagram_fails', [
    ('elbow', 'belw'),
    ('elbow', 'belowa'),
    ('a', ''),
    ('', 'a'),
    ('a gentleman', 'elegant mn'),
    ('a gentleman', 'elegant mana')
])
def test_is_anagram_fails(word, anagram_fails):
    assert not is_anagram(word, anagram_fails)