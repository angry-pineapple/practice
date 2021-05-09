# Reverse words in a string
"""
Steps:
 1.original string-              my name is adam
 2.Reverse the entire string-    mada si eman ym
 3.reverse by words -            adam is name my

TODO
 Handle space in between input string -- Done

"""


def reverse_string(my_string):
    return my_string[::-1]


def reverse_words(reversed_string):
    words = []
    my_stack = []
    mod_string = ""
    # put chars in a stack , when reached a space, pop all out and add to words list
    found_space = False
    for char in reversed_string:
        if char == " ":
            if found_space is True:
                continue
            found_space =True
            word = ""
            while len(my_stack) != 0:
                word += my_stack[-1]
                my_stack = my_stack[:-1]
            words.append(word)
        else:
            found_space = False
            my_stack.append(char)
    # Pop any remaining characters from stack in reversed manner
    word = ""
    while len(my_stack) != 0 :
        word += my_stack[-1]
        my_stack = my_stack[:-1]
    words.append(word)
    for w in words:
        mod_string += w + " "

    return mod_string.strip()


def reversed_string_by_words(my_string):
    # Reverse entire string
    reversed_string = reverse_string(my_string)
    reversed_words_string = reverse_words(reversed_string)
    return reversed_words_string

if __name__ == "__main__":
    my_string = "  Bob    Loves  Alice   "
    word_reversed_string = reversed_string_by_words(my_string)
    print(f"my original string = {my_string}, len-{len(my_string)}")
    print(f"string with reversed words: {word_reversed_string}, len-{len(word_reversed_string)}")
