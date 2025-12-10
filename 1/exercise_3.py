import re


def normalization(input_str: str) -> str:
    result = input_str

    result = result.lower().strip()
    result = re.sub(r"\.*\s*\.+\s*\.*", ". ", result)
    result = re.sub(r"\s+", " ", result)

    # TODO: remove the dot at the start of string then upper the first letter
    # result = result[0].upper() + result[1:]

    return result


def main():
    print(normalization(input("input a random string contain dots: ")))


if __name__ == "__main__":
    main()
