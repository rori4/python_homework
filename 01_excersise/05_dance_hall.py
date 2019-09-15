length = float(input())
width = float(input())
w_side = float(input())
room = (length * 100) * (width * 100)
wardrobe = (w_side * 100) ** 2
benches = room / 10
free_space = room - wardrobe - benches
dancers = free_space / 7040
print(int(dancers))
