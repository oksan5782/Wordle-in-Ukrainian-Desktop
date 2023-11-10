from project import choose_word, word_exists, too_short
from all_words import ALL_WORDS
import pytest



# Choose random 5-letter word
def test_choose_word():
    assert isinstance(choose_word(), str) == True
    assert len(choose_word()) == 5


# Check if the word is in global list or not
def test_word_exists():
    assert word_exists("бузок") == True
    assert word_exists("AAAAA") == False
    assert word_exists(12) == False


# Check if check word length is less than 5 letters
def test_too_short():
    assert too_short(5) == False
    assert too_short(2) == True
    with pytest.raises(TypeError):
       too_short("ABC")

