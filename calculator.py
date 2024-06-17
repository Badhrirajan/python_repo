def add(x,y):
    x = int(input("Enter the x value : "))
    y = int(input("Enter the y value : "))
    print(x + y)

def sub(x,y):
    x = int(input("Enter the x value : "))
    y = int(input("Enter the y value : "))
    print(x - y)

def Mul(x,y):
    x = int(input("Enter the x value : "))
    y = int(input("Enter the y value : "))
    print(x * y)

def Div(x,y):
    x = int(input("Enter the x value : "))
    y = int(input("Enter the y value : "))
    print(x / y)

def square(x):
    x = int(input("Enter the x value : "))
    print(x ** 2)

def cube(y):
    y = int(input("Enter the y value : "))
    print(y ** 3)

print("""1.Add, 2.Sub, 3.Mul, 4.Div,5.Square,6.Cube""")

while True:
    user_choice = int(input("Enter the choice : "))
    if user_choice == 1:
        add(x,y)
    elif user_choice == 2:
        sub(x,y)
    elif user_choice == 3:
        Mul(x,y)
    elif user_choice == 4:
        Div(x,y)
    elif user_choice == 5:
        square(x)
    elif user_choice == 6:
        cube(y)
    else:
        print("Invalid Option")

