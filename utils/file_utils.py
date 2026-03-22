
def read_lines(filename) -> list[str]:
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, lines) -> None:
    with open(filename, mode="r") as file:
        file.write(lines)


def count_words(filename) -> dict:
    result = {}
    with open(filename, mode="r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result


