user1 = int(input("Enter a Positive number : "))
user2 = int(input("Enter a Positive number : "))
user3 = int(input("Enter a Positive number : "))
user4 = int(input("Enter a Positive number : "))
user5 = int(input("Enter a Positive number : "))
list = [user1, user2, user3, user4, user5]
for i in list:
    print(i)
if (user1 <= 0 or user2 <= 0 or user3 <= 0 or user4 <= 0 or user5 <= 0):
    print("Please enter valid or Positive number")
else:
    total = user1+user2+user3+user4+user5
    x = open("mydata.txt", "a")
    print("Inputs given by 5 users:", list)
    print("Inputs given by 5 users are", list, file=x)
    print("total amount is :", total)
    print(total, file=x)
