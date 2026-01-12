import math


class Circle:
    def __init__(self, radius):
        # 半径を保存
        self.radius = radius

    def area(self):
        # 面積を計算: π × r²
        result = math.pi * self.radius**2
        return round(result, 2)

    def perimeter(self):
        # 周囲長を計算: 2 × π × r
        result = 2 * math.pi * self.radius
        return round(result, 2)


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
