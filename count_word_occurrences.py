def count_word_occurrences(text, word):

    if len(text) > 0:
        check_text = text.lower()
        print(check_text)
        return check_text.count(word.lower())
    else:
        return 0


print(count_word_occurrences("Python is a versatile programming language.", "Python"))
