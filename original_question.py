'''
INSTRUCTIONS: Given a string containing words seperated by a space, return a result with all characters lowercase
except the first character of every word.


CONSTRAINTS:
Returned string contains words seperated by a space


EXAMPLE:
Input: this is a sentence
Output: This Is A Sentence
'''


# Possible Solution
def capitalize_words(sentence):
    words = sentence.split()
    new_sentence = []

    for word in words:
        lowercase_word = word.lower()
        capitalized_word = lowercase_word.capitalize()
        new_sentence.append(capitalized_word)

    return " ".join(new_sentence)
