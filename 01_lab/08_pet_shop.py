dogs = int(input())
other = int(input())
end_price = float(dogs * 2.50 + other * 4)
formatted_price = format(end_price, '.2f')
print(f'{formatted_price} lv.')
