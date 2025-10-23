import math
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def circumference(self):
        return 2 * math.pi * self.r

    def intersects_with(self, other):
        """
        Returns True if this circle intersects with the other circle.
        """
        center_dist = math.hypot(self.x - other.x, self.y - other.y)
        return abs(self.r - other.r) <= center_dist <= (self.r + other.r)

    def __str__(self):
        return f"Circle(center=({self.x}, {self.y}), radius={self.r})"

def plot_circles(circle1, circle2):
    fig, ax = plt.subplots()
    c1 = plt.Circle((circle1.x, circle1.y), circle1.r, color='blue', fill=False, label="Circle 1")
    c2 = plt.Circle((circle2.x, circle2.y), circle2.r, color='red', fill=False, label="Circle 2")
    ax.add_artist(c1)
    ax.add_artist(c2)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(min(circle1.x, circle2.x) - max(circle1.r, circle2.r) - 2, max(circle1.x, circle2.x) + max(circle1.r, circle2.r) + 2)
    ax.set_ylim(min(circle1.y, circle2.y) - max(circle1.r, circle2.r) - 2, max(circle1.y, circle2.y) + max(circle1.r, circle2.r) + 2)
    plt.legend([c1, c2], ["Circle 1", "Circle 2"])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    c1 = Circle(0, 0, 5)
    c2 = Circle(7, 3, 4)

    print(f"{c1} => Area: {c1.area():.2f}, Circumference: {c1.circumference():.2f}")
    print(f"{c2} => Area: {c2.area():.2f}, Circumference: {c2.circumference():.2f}")

    if c1.intersects_with(c2):
        print("The circles intersect!")
    else:
        print("The circles do not intersect.")

    plot_circles(c1, c2)
