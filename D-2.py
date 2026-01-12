import math  # sqrt（平方根）を使うために必要


class Rectangle:
    def __init__(self, height, width):
        # 高さと幅を保存
        self.height = height
        self.width = width

    def area(self):
        # 面積を計算
        return self.height * self.width

    def diagonal(self):
        # 対角線を計算: √(高さ² + 幅²)
        return math.sqrt(self.height**2 + self.width**2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
