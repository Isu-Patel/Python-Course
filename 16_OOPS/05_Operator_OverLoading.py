class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        return (f"X is {self.x} and Y is {self.y}")
    
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is the sum of p1 and p2
p = p1 + p2 # We overloaded the + operator by writing the __add__ function
p.print_point() # This will print the point p