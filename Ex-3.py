#function
def greet():
    print("Hi there!")
    print("Welcome aboard")
greet()

#agruments
def greeting(first_name, last_name):
    print(f"Hi {first_name}, {last_name}")
    print("Welcome aboard!")
greeting("Tarana", "Mahmud")

#Keyword arguments
def increment (number, by):
    return number+by
print(increment(2, by=1))

#creating class
class Point:
    def draw(self):
        print("draw")
point=Point()
print(type(point))
print(isinstance(point, Point))