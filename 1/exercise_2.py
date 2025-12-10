import math


def get_sum(num: int) -> float:
    if num < 1:
        return 0.0

    res = 0.0

    for i in range(1, num + 1):
        res += 1 / math.factorial(2 * i - 1)

    return float(res)


def main():
    input_int = int(input("Enter a number: "))
    print(get_sum(input_int))


if __name__ == "__main__":
    main()
