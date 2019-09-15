square_meters = float(input())
price = square_meters * 7.61
discount = price * 0.18
final_price = price - discount
print(f'The final price is: {format(final_price, ".2f")} lv.')
print(f'The discount is: {format(discount, ".2f")} lv.')
