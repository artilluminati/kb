def calculate_triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

side1 = float(input("Введите длину стороны 1: "))
side2 = float(input("Введите длину стороны 2: "))
side3 = float(input("Введите длину стороны 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    area = calculate_triangle_area(side1, side2, side3)
    print(f"Площадь треугольника: {area}")
else:
    print("Невозможный треугольник. Сумма двух длин любых сторон должна быть больше длины третьей.")