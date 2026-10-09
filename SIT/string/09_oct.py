# 1. Wap to input a string and toggle the cases (convert uppercase to lowercase and via versa).
def toggle_case(text: str) -> str:
    new_text: str = ''

    for c in text:
        if c.islower():
            new_text = new_text + c.upper()
        elif c.isupper():
            new_text = new_text + c.lower()
        else:
            new_text = new_text + c

    return new_text


# 2. Wap to create a list of fruits name, and check how many are more then 5 characters in length.
def display_fruits(fruits: list[str]) -> int:
    """Print the names of fruits that have more than 5 characters."""
    for f in range(len(fruits) - 1, -1, -1):
        if len(fruits[f].strip()) < 5:
            fruits.pop(f)
    # print(fruits)
    return len(fruits)


if __name__ == '__main__':
    t: str = input('Enter your text:')
    # print(toggle_case(t))
    print(display_fruits(t.split(',')))
