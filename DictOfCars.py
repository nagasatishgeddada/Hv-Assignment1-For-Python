Car = {}
Brand_Name = input("Enter a Car Brand Name : ")
Color = input("Enter a  Car Color : ")
Car[Brand_Name] = Color
x = open("mycar.txt", "a")
print(Car)
print(" BrandName and Color", file=x)
print(Car, file=x)
