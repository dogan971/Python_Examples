# Denklem: ax^2 + bx + c
# Deltayı Hesaplama: b**2-4*a*c
# Birinci Kök : (-b - delta ** 0.5) / (2*a)
# İkinci Kök : (-b + delta ** 0.5) / (2*a)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)
print(f"1.kök {x1}")
print(f"2.kök {x2}")