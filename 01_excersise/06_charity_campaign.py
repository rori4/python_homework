campaign_days = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
goods_total = (cakes * 45) + (waffles * 5.80) + (pancakes * 3.20)
daily_profit = goods_total * cookers
total_profit = 7 / 8 * (daily_profit * campaign_days)
print(f'{total_profit:.2f}')
