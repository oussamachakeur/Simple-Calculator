#CALCULATOR  

def sum(a,b):
    sume = a+ b 
    print(sume)

def sub(a,b):
    sube = a- b 
    print(sube)

def mul(a,b):
    mule = a* b
    print(mule)

def div(a,b):
    dive = a/ b
    print(dive)

print("hello to the calculator ")
print("u can start")
running = True
while running is True:
    a=float(input())   
    operation = input("enter (+ , - , x , / ): ")       
    b= float(input())
    if operation == "+":
        sum(a,b)
    elif operation == "-":
        sub(a,b)
    elif operation == "x":
        mul(a,b)
    elif operation == "/":
        div(a,b)
    cntn=input("do you wanna continue? (yes/no): ").lower()
    if cntn == "yes":
        continue
    else:
        print("thanks for using us ")
        running = False

