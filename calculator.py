def add(x,y):
    print(x + y)

def sub(x,y):
    print(x - y)

def Mul(x,y):
    print(x * y)

def Div(x,y):
    print(x / y)

def percent(x):
    print(x / 100 * 100)

x = int(input("Enter the x value : "))
y = int(input("Enter the y value : "))

print("""1.Add, 2.Sub, 3.Mul, 4.Div,5.Percent""")

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
            percent(x)
    else:
        print("Invalid Option")

