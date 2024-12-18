list_prices = [75, 88, 32, 5]


def getting_price(prices: list[float]) -> float:
    total_price = 0
    for price in prices:
        total_price += price
    return total_price


store = getting_price(list_prices)
print(store)


def can_buy(budget: float, price: float) -> bool:
    return budget >= price


shop = can_buy(budget=50, price=100)
print(shop)


def do(items: list[str]) -> list[str]:
    list_of_words = []
    for item in items:

        if item not in list_of_words:
            list_of_words.append(item)
    return list_of_words


words = do(items=['jnl', 'ef', 'ef'])
print(words)
