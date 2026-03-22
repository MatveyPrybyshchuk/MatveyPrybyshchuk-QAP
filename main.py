import utils.math_utils
from utils.file_utils import read_lines, write_lines, count_words


if __name__ == '__main__':
    # insert = int(input("Please insert num: "))

    # print(f"squareed: {utils.math_utils.square(insert)}")
    # print(f"cubed: {utils.math_utils.cube(insert)}")
    # print(f"is even: {utils.math_utils.is_even(insert)}")

    read_lines("source.txt")
    write_lines("source.txt", "new_line")
    print(count_words("source.txt"))
