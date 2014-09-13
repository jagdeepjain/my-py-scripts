__author__ = 'jagdeepjain'


import sys


def snake(pattern, i):
    print("You are rolling pattern=\'%s\' from %dth position." % (pattern, i))
    print(pattern[i:], end="")
    print(pattern[0:i])


def main(argv):
    pattern = str(argv[0])
    try:
        i = int(argv[1])
    except ValueError:
        print("First value should be the string you want to roll & second "
              "should be an integer number less then or equal to length of string.")
        exit()
    pattern_length = len(pattern)
    if i > pattern_length:
        print("Rolling value is outside length of pattern.")
        exit()
    snake(pattern, i)


if __name__ == '__main__':
    main(sys.argv[1:])


