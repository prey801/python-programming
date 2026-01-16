class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircumference(self):
        return 2 * 3.14 * self.radius


# Example usage
radius = float(input("Enter the radius of the circle: "))
c = Circle(radius)

print("Area of the circle:", c.getArea())
print("Circumference of the circle:", c.getCircumference())
