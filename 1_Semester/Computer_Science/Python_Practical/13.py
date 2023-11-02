# Write A Program to define a class Point with coordinates x and y as attributes. Create relevant methods and print the objects. Also define a method distance to calculate the distance between any two point objects.
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Print_point(self):
        print("Coordinates of the point ({},{})".format(self.x,self.y))
    def Calculate_Distance(self,self1):
        dx=self.x-self1.x
        dy=self.y-self1.y
        distance=(dx**2+dy**2)**0.5
        return distance
choice='y'
while choice=='y':
    print("Enter 1st Co-ordinates: ")
    p1 = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))
    print("Enter 2nd Co-ordinates: ")
    p2 = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))
    p1.Print_point()
    p2.Print_point()
    print(p1.Calculate_Distance(p2))
    choice=input("Do you want to use again(y/n):").lower()
print("Thank you for using my program")
