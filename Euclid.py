def GCD(a,b):
    
    if b == 0:
        print('НОД чисел',a_answer,'и',b_answer,'=',a)
        
    else:
        c=a
        a=b
        b=c%b
        return GCD(a,b)
        
print('Введите два числа, для нахождения их НОД')

inpt=input()
inpt=inpt.split()
a=int(inpt[0])
b=int(inpt[1])
a_answer=a
b_answer=b
d=GCD(a,b)
