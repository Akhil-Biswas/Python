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


# 3. WAP to create a string and return the position of vowels,whenever found.
def display_vowel_position(text: str):
    memory = {}
    for i in range(len(text)):
        if text[i].lower() in 'aeiou':
            if text[i] not in memory:
                memory[text[i]] = []
            memory[text[i]].append(i)
    return memory


# 4. WAP to create a string and replace all vowels with `0` **zero**.
def replace_string(text: str) -> str:
    new_text: str = ''
    for i in text:
        if i.lower() in 'aeiou':
            new_text = new_text + '0'
        else:
            new_text = new_text + i
    return new_text


# 5.  WAP to input a string and print the __ in pyramid effect
def display_pyramid(text: str) -> None:
    for i in range(len(text)):
        print(text[: i + 1])


if __name__ == '__main__':
    t: str = input('Enter your text:')
    # print(toggle_case(t))
    # print(display_fruits(t.split(',')))
    # print(replace_string(text=t))
    # print(display_vowel_position(t))
    # display_pyramid(text=t)
