import sys


def count_characters(text):
    """
    Count the number of uppercase letters, lowercase letters, punctuation
    marks, spaces, and digits in the given text.

    :param text: The text to be analyzed.
    :type text: str
    :return: None
    """
    uppercase = 0
    lowercase = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for character in text:
        if "A" <= character <= "Z":
            uppercase += 1
        elif "a" <= character <= "z":
            lowercase += 1
        elif character in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punctuation += 1
        elif character == " " or character == "\n":
            spaces += 1
        elif character in "0123456789":
            digits += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{uppercase} upper letters")
    print(f"{lowercase} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main function to handle input and call the count_characters function.

    :returns: None
    """

    input_arg = ""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 2:
            input_arg = sys.argv[1]
        elif len(sys.argv) < 2 or sys.argv[1] is None:
            input_arg = input("What is the text to count?\n")
            input_arg += "\n"
        count_characters(input_arg)
    except AssertionError as e:
        print("AssertionError:", e)
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    main()
