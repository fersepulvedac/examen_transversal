from statistics import mean, geometric_mean
from random import randint

print(geometric_mean([10, 25, 46, 78]))

print(min([10, 25, 46, 78]))

nombres = ["Juan abarca", "Fernando Sepulveda"]

for nombre in nombres:
    print(f"{nombre.ljust(20)} {str(randint(100, 5000)).ljust(10)}")
    
# with open("reporte_sueldos.csv", "w", newline="", encoding="utf8") as archivo: