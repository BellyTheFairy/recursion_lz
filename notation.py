base = int(input(''))    # 
numb = int(input(''))    #
digits = '0123456789ABCDEF'
result = ''

def convert(numb, base):
    result = ''
    while numb > 0:
        digit = numb % base
        result = digits[digit] + result
        numb //= base
