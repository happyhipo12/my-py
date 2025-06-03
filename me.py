def add(a,b):
    return a+b

while True:   
    x=float(input("Enter first number: "))
    y=float(input("Enter second number: "))
    print("The sum is: ", add(x,y))
    
    again=input("Do you want to add more numbers? (yes/no): ").strip().lower()
    if again !='yes':
        print("byeee!!!")
        break
    