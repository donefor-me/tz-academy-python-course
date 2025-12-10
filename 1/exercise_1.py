import re

MONTHS_31_DAYS: list[int] = [1, 3, 5, 7, 8, 10, 12]
MONTHS_30_DAYS: list[int] = [4, 6, 9, 11]


def is_leaf_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_last_date_of_month(month: int, year: int) -> int:
    if month == 2:
        return 29 if is_leaf_year(year) else 28
    if month in MONTHS_31_DAYS:
        return 31
    if month in MONTHS_30_DAYS:
        return 30

    return -1


def is_not_positive_digit(input_str: str) -> bool:
    return not input_str.isdigit() or int(input_str) <= 0


def get_adjacent_dates(date_str: str) -> tuple[str, str]:
    """
    :param date_str: a date string with YYYY-MM-DD format
    :return: tuple[before_date: str, after_date: str]
    """
    date_regex = r"^\d+-\d{1,2}-\d{1,2}$"
    is_valid = re.match(date_regex, date_str)
    if not is_valid:
        return "", ""

    date_arr = date_str.split("-")
    _year = int(date_arr[0])
    _month = int(date_arr[1])
    _date = int(date_arr[2])

    last_date_of_month = get_last_date_of_month(_month, _year)
    last_date_of_prv_month = get_last_date_of_month(_month - 1, _year)

    if not is_leaf_year(_year):
        if _month == 2 and _date == 29:
            return "", ""

    if last_date_of_month == -1 or _date > last_date_of_month:
        return "", ""

    before = f"{_year}-{_month}-{_date - 1}"
    after = f"{_year}-{_month}-{_date + 1}"

    if _date == 1:
        if _month == 1:
            before = f"{_year - 1}-12-31"
        else:
            before = f"{_year}-{_month - 1}-{last_date_of_prv_month}"

    if _date == last_date_of_month:
        if _month == 12: # happy new year
            after = f"{_year + 1}-01-01"
        else:
            after = f"{_year}-{_month + 1}-01"

    return before, after


def terminal_execute() -> None:
    exit_key = "c"

    is_first_run = True
    int_month: int | None = None
    int_date: int | None = None

    while True:
        if is_first_run:
            print(f"press {exit_key} to exit")
            is_first_run = False

        # year input and validation
        raw_year = input("input year: ")
        if exit_key == raw_year:
            break
        if is_not_positive_digit(raw_year):
            print("invalid year value")
            continue

        int_year = int(raw_year)

        # month input and validation
        while True:
            raw_month = input("input month: ")
            if exit_key == raw_month:
                break
            if is_not_positive_digit(raw_month):
                print("invalid month value")
                continue
            int_month = int(raw_month)
            if int_month > 12:
                print("month cannot be greater than 12")
                continue
            else:
                break

        if exit_key == raw_month:
            break

        # date input and validation
        while True:
            raw_date = input("input date: ")
            if exit_key == raw_date:
                break
            if is_not_positive_digit(raw_date):
                print("invalid date value")
                continue
            int_date = int(raw_date)
            if int_month == 2 and int_date > 28:
                print("February only allow date from 1 to 28")
                continue
            if int_month in MONTHS_30_DAYS and int_date > 30:
                print(f"month {int_month} only have 30 days")
                continue
            if int_month in MONTHS_31_DAYS and int_date > 31:
                print(f"month {int_month} only have 31 days")
                continue
            else:
                break

        if exit_key == raw_date:
            break

        # final result
        date_month_year = f"{int_year}-{int_month}-{int_date}"
        print(date_month_year)
        date_before, date_after = get_adjacent_dates(date_month_year)
        print(f"date before: {date_before}")
        print(f"date after: {date_after}")
        break


def main():
    terminal_execute()


def _test_get_adjacent_dates() -> None:
    print(get_adjacent_dates("2025-01-01"))
    print(get_adjacent_dates("2025-12-31"))
    print(get_adjacent_dates("2025-1-31"))
    print(get_adjacent_dates("2025-2-29"))
    print(get_adjacent_dates("2025-2-28"))
    print(get_adjacent_dates("2025-4-1"))
    print(get_adjacent_dates("2025-4-30"))
    print(get_adjacent_dates("2025-4-31"))
    print(get_adjacent_dates("2025-7-1"))
    print(get_adjacent_dates("2025-07-31"))


if __name__ == '__main__':
    main()
