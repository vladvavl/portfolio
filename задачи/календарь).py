a =int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("високосный")
    b = True
else :
    print("не високосный")
    b=False
a = int(input())
if a in (1,3,5,7,9,11,12):
    print(31)
elif (a == 2 ) :
    if b == True:
       print(29)
    else:
       print(28)
elif (a<13):
  print(30)
else :
  print ("нет месяца")



    

