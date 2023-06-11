def next(): 
    num1=float(input('enter num 1 : '))
    num2=float(input('enter num 2 : '))
    cal=input('enter the operator( +,-,*,/ )')

    if cal=='+':
        print('addition : ',num1+num2)
    elif cal=='-': 
        print('subtraction : ',num1-num2)
    elif cal=='*':
        print('multipilication : ',num1*num2)
    elif cal=='/':
        print('division : ',num1/num2)
    else: 
        print(f'{cal} not a oprator founded')
next()
x=input('do u want to run again')
if x=='yes': 
    next()
else:
    print('thanks for using ')