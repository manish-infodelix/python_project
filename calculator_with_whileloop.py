
# while loop calculator ( 2 digits) with exit

while True:
    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. power (**)")
    print("6. Exit ")
    
    x= int(input("enter the choice "))
    if(x>0 and x<=5):
           
           a= int(input("enter the 1st value = "))
           b= int(input("enter the 2nd value = "))
           if (x==1):
                  c=a+b
                  print(c)
           elif (x==2):
                  c=a-b
                  print(c)
           elif (x==3):
                  c=a*b
                  print(c)
           elif (x==4):
                  c=a/b
                  print(c)
           elif (x==5):
                  c=a**b
                  print(c)
    elif(x==6):
        break
    else:
        print("try again")


        
