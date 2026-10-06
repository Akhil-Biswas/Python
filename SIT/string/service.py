# 1. Wap to input a string and count the no of uppercase , lowercase & digits
def count_char(text: str) -> None:
    """That function count number of uppercase , lowercase & digits in string"""

    # txt: str = input('Enter Your Text:')
    uppercase: int = 0
    lowercase: int = 0
    digits: int = 0

    for i in txt:
        if i.isupper():
            uppercase = uppercase + 1
        elif i.islower():
            lowercase = lowercase + 1
        elif i.isdigit():
            digits = digits + 1

    print('Uppercase:', uppercase)
    print('Lowecase:', lowercase)
    print('Degits:', digits)


# 2. Wap to input A string and print every character
#    i. on a separate line
#    ii. Same line separated by comma
def print_char(txt: str):
    # txt: str = input('Enter Your Text:')
    for i in txt:
        print(i)

    print('----------------')
    for i in txt:
        print(i, end=', ')
    print()


# 3. Wap to input string & chack valide password according to the following:
#    i. minimum length of 8
#    ii. Must have one upper case character
#    iii. Must have one digits

# def check_password(password: str):
#     if len(password) < 8:
#         print('Minimum length 8')
#         return
#     for i in password:
#         if not i.isupper:
#             print('Minimum length 8')
#             return


if __name__ == '__main__':
    txt: str = input('Enter Your Text:')
    # count_char(txt=txt)
    print_char(txt=txt)
