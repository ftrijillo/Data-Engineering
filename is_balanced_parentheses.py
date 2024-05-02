def is_balanced_parentheses(s):
    brackets = ["()", "{}", "[]"]
    while any(x in s for x in brackets):
        for br in brackets:
            s = s.replace(br, "")
    return not s


print(is_balanced_parentheses("([])"))
