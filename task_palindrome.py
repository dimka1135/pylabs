import re
def is_palindrome(s):
    pattern = r'[\W_]*'  
    s = re.sub(pattern, '', str(s).lower())
    return list(s) == list(reversed(s))