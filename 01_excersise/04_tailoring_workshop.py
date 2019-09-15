tables = int(input())
length = float(input())
width = float(input())
table_tops = tables * (length + 2 * 0.30) * (width + 2 * 0.3)
area = tables * (length / 2) * (length / 2)
usd_price = table_tops * 7 + area * 9
bgn_price = usd_price*1.85
print(f'{usd_price:.2f} USD')
print(f'{bgn_price:.2f} BGN')
