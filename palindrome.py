

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()    #Clean the spaces and lowercase the letters
    return string == string[::-1]

def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run() 

#Then we run the comando : > mypy palindrome.py --check-untyped-defs
# This comand show us in terminal all the type errors.