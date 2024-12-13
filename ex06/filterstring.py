import sys
from ft_filter import ft_filter


def filter_string(text, length):
    return list(ft_filter(lambda word: len(word) > length, text.split()))


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        s = sys.argv[1]
        n = int(sys.argv[2])

        assert isinstance(s, str), "the arguments are bad"
        assert isinstance(n, int), "the arguments are bad"

        print(filter_string(s, n))

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
