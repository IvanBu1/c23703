# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
a1 = a

print(a // b)

z = 0
while a >= b:
    z += 1
    a -= b
print("Целочисленное деление " + str(a1) + " на " + str(b) + " дает " + str(z))