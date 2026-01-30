import math

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 )
    def midpoint(self, other_point):
        mid_x = (self.x + other_point.x) / 2
        mid_y = (self.y + other_point.y) / 2
        return Point(mid_x, mid_y)  
        

p1 = Point(3, 4)

p1.distance_from_origin()
print(p1.distance_from_origin())

mid = p1.midpoint(Point(5, 11))
print(f"Midpoint: ({mid.x}, {mid.y})")

# print(p1.x, p1.y)
# p1.x = 10
# p1.y = 20
# print(p1.x, p1.y)