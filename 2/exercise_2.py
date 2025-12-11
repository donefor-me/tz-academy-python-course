# * Yêu cầu:
#   * a. Tạo một dict `product_map` từ `products` để tra cứu nhanh theo `product_id` với dạng:
#         {
#             1: {"name": "Ban Phim", "price": 250_000},
#             2: {"name": "Chuot", "price": 150_000},
#             ...
#         }
#   * b. Với mỗi hóa đơn trong `orders`, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới `"total"` trong từng dict hóa đơn
#     * Hints:
#       * items là list các product_id
#       * tra giá ở product_map (dict)
#       * cộng dồn
#   * c. In ra danh sách hóa đơn theo format:
#         HD01: 3 san pham, Tong tien = ...
#         HD02: ...
#   * d. Tạo một set `all_products_sold` chứa tất cả `product_id` đã từng được bán trong mọi hóa đơn, sau đó in ra:
#       So luong san pham khac nhau da ban: <len(all_products_sold)>
class Product:
    def __init__(self, name: str, product_price: float | int) -> None:
        self.name = name
        self.product_price = product_price


products = [
    (1, "Ban Phim", 250000),
    (2, "Chuot", 150000),
    (3, "Man Hinh", 3000000),
    (4, "Tai Nghe", 500000),
]

orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

product_map: dict[int, Product] = {}
bills: dict[str, int] = {}  # [order id, total cost]


# a
def exercise_a() -> None:
    print("- a")
    for product in products:
        product_id, product_name, price = product
        product_map[product_id] = Product(product_name, price)

    print(product_map)

    try:
        print(product_map[1])
    except KeyError as e:
        print(e)


# b
def exercise_b() -> None:
    print("- b")
    for order in orders:
        total_cost: int = 0
        for product_id in order["items"]:
            total_cost += product_map.get(product_id).product_price
        bills[order["order_id"]] = total_cost

    print(bills)


# c
def exercise_c() -> None:
    print("- c")
    order_formated: list[dict[str, str]] = []
    for order in orders:
        order_id = order["order_id"]
        formated_total_cost = "{:,}".format(bills[order_id])
        print(f"{order_id}: Total cost = {formated_total_cost}")


# d
def exercise_d() -> None:
    print("- d")
    all_products_sold: set[str] = set()
    for product_id in [product_id for order in orders for product_id in order["items"]]:
        all_products_sold.add(product_id)

    print(f"Products sold: {all_products_sold}")
    print(f"Total products sold: {len(all_products_sold)}")


def main():
    exercise_a()
    exercise_b()
    exercise_c()
    exercise_d()


if __name__ == "__main__":
    main()
