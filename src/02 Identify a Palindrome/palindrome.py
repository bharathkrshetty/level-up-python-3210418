import re


def is_palindrome(phrase):
    phrase1 = phrase.replace(" ", "")
    phrase2 = ""
    for char in phrase1:
        if (char.isalnum()):
            phrase2 = phrase2+char
            phrase2 = phrase2.lower()
    print(phrase2)
    for i in range(0, int(len(phrase2)/2)):
        if phrase2[i] != phrase2[len(phrase2)-i-1]:
            return False
        return True


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
