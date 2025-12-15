# 1. Chương trình hỏi người dùng:
# ```text
# Nhập tên file cần phân tích:
# ```
#
# 2. Đọc toàn bộ nội dung file, chuẩn hóa:
# * chuyển hết về chữ thường (`lower()`)
# * bỏ các dấu câu cơ bản: `.,;:?!()[]` (có thể dùng `replace`)
#
# 3. Tách từ theo dấu cách, đếm số lần xuất hiện của từng từ
# 4. In ra:
# * Tổng số từ
# * Top 10 từ xuất hiện nhiều nhất cùng số lần xuất hiện
import re
from collections import Counter


def file_reader() -> list[str]:
    try:
        with open("3/1/texts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        _result: list[str] = []

        for line in lines:
            _result.append(line)

        return _result

    except FileNotFoundError:
        print("File not found")
        return []
    except IOError:
        print("IO Error")
        return []


def string_normalization(list_str: list[str]) -> str:
    text = " ".join(list_str)
    text = text.lower()
    chars_should_remove = r'[.,;:?!()\[\]]'
    text = re.sub(chars_should_remove, '', text)
    return text


def get_total_word(counter: Counter) -> int:
    return sum(counter.values())


def count_words(text: str) -> Counter:
    words = text.split()
    return Counter(words)


def main() -> None:
    file_lines = file_reader()
    normalization_text = string_normalization(file_lines)
    word_counter = count_words(normalization_text)
    total_words = get_total_word(word_counter)
    top_10 = word_counter.most_common(10)

    print(f"total word: {total_words}")
    print("top 10: ")
    for word, count in top_10:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
