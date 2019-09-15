whiskey_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
whiskey_quantity = float(input())

rakia_price = whiskey_price / 2
wine_price = 0.6 * rakia_price
beer_price = 0.2 * rakia_price

total = whiskey_price * whiskey_quantity + \
        beer_price * beer_quantity + \
        rakia_price * rakia_quantity + \
        wine_price * wine_quantity
print(f'{total:.2f}')
