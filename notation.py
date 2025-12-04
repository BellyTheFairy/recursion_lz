base = int(input('Введите основание системы счисления: '))
num = int(input('Введите число: '))

def notation(N: int, T: int) -> str:
    if N == 0:
        return '0'

    digit = ''
    while N > 0:
        N, r = divmod(N, T)
        if r > 9:
            r = chr(ord('A') + r - 10)
        digit = str(r) + digit
    return digit



print(f'Число {num} в системе счисления с основанием {base}: {notation(num, base)}')
