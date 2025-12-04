inp = input('Введите два числа ')
inp_is = inp.split()
inp_1 = int(inp_is[0])
inp_2 = int(inp_is[1])

def gcd(a:int, b:int) -> int:
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)
        
print(f'Нод чисел {inp_1} и {inp_2}: {gcd(inp_1, inp_2)}')
