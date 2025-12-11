# * Yêu cầu:
#   * a. Tạo một dict `user_map` từ `users`, map `user_id` sang `name`
#     ```text
#         Ví dụ:
#         {
#             "U01": "Alice",
#             "U02": "Bob",
#             "U03": "Charlie",
#         }
#     ```
#   * b. Dùng vòng lặp duyệt `posts.items()` để in ra:
#     ```text
#         [P01] Hoc Python co ban - Alice - Tags: python, beginner
#     ```
#     * c. Tạo một set `all_tags` chứa toàn bộ tag xuất hiện trong mọi bài viết
#       * Hints: duyệt từng `post`, lấy `post["tags"]` (set), dùng `update()` để dồn vào `all_tags`
#     * d. Tạo một dict `tag_counter` để đếm số bài viết chứa mỗi tag
#       ```text
#         Ví dụ:
#         {
#               "python": 2,
#               "beginner": 1,
#               "data-structure": 1,
#               "web": 1,
#               "frontend": 1,
#         }
#       ```
from collections import defaultdict

users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}


user_list: dict[str, str] = {}


# a
def exercise_a() -> None:
    print("- a")
    for user in users:
        user_id, user_name = user
        user_list[user_id] = user_name
    print(user_list)


# b
def exercise_b() -> None:
    print("- b")
    try:
        for post_id in posts:
            post_title = posts[post_id]["title"]
            post_author_id = posts[post_id]["author_id"]
            post_author_name = user_list[post_author_id]
            tags = posts[post_id]["tags"]
            print(
                f"[{post_id}] {post_title} - {post_author_name} - Tags: {", ".join(tags)}!"
            )
    except KeyError:
        pass


# c
def exercise_c() -> None:
    print("- c")
    all_tags: set[str] = set()
    try:
        for tag in [tag for post_id in posts for tag in posts[post_id]["tags"]]:
            all_tags.add(tag)
    except KeyError:
        pass
    print(all_tags)


# d
def exercise_d() -> None:
    print("- d")
    tag_counter: dict[str, int] = {}

    for tag in [tag for post_id in posts for tag in posts[post_id]["tags"]]:
        if tag not in tag_counter:
            tag_counter[tag] = 1
        else:
            tag_counter[tag] += 1

    print(tag_counter)


def main():
    exercise_a()
    exercise_b()
    exercise_c()
    exercise_d()


if __name__ == "__main__":
    main()
