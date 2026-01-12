import math


class Square:
    def __init__(self, side):
        # 一辺の長さを保存
        self.side = side

    def area(self):
        # 面積を計算: 辺²
        return self.side**2

    def diagonal(self):
        # 対角線を計算: 辺 × √2
        result = self.side * math.sqrt(2)
        return round(result, 2)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
