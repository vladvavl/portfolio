while True:
    b = int(input("введите чсло"))
    if b > 0 and b <11:
        for a in range(1,11):
            print (a,"*",b,"=",a*b )
            # print(f'{a} * {b} = {a*b}')
        break
    else:
         print("вы ввели не правильное число")


    

