
# while lopp calculator with exit

while True:
    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit ")
    
    x= int(input("enter the choice "))
    if(x>0 and x<=4):
           
           a= int(input("enter the value"))
           b= int(input("enter the value"))
           if (x==1):
                  c=a+b
                  print(c)
           elif (x==2):
                  c=a-b
                  print(c)
           elif (x==3):
                  c=a*b
                  print(c)
           elif (x==5):
                  c=a/b
                  print(c)

    elif(x==5):
        break
    else:
        print("try again")


        
