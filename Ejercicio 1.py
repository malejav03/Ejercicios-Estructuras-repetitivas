n = int(input("Digite el primer número: "))
m = int(input("Digite el segundo número: "))

for i in range(m):
    num = (i+1)
    multi = n * num
    print(f"{n} x {num} = {multi}")