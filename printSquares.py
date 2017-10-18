#Gary Li
#10/18/17
#printSquares

def printSquares(num1,num2):
    for i in range(1,num1+1):
        print('+--'*num2+'+')
        print('|  '*num2+'|')
    print('+--'*num2+'+')
    
printSquares(10,4)
