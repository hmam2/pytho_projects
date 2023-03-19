
def calculater (a,b):
    a = float(input('enter the first number:'))
    operation = input("operation you need : ")
    b = float(input('enter the second number:'))
    if operation == "+" :
        plus_result = a + b 
        print (f'{a} + {b}  = {plus_result}')
    elif operation == "-" :
        minus_result = a - b 
        print (f'{a} - {b}  = {minus_result}')
    elif operation == "*":
        result = a * b 
        print (f'{a} * {b}  = {result}')
    elif operation == '/':
        dvide_ruslt = a / b 
        print (f'{a} / {b}  = {dvide_ruslt}')
        
    

def calculat_agine():
    question = input('do you want make operation else ?')
    if question == 'yes':
        return True
    else:
        return False
       
     

calculater(a = "",b=" ")

while calculat_agine():
    print('------------------------------------')
    calculater(a='',b='')
    
print('good bye')