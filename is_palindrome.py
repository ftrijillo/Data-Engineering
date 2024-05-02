def is_palindrome(string):
    rev_string = string[::-1]
    return rev_string == string


print(is_palindrome("adida"))
