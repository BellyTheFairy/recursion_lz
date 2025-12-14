def pascal_triangle(n):
    if n == 1:  
        return [[1]]
    triangle = pascal_triangle(n - 1)
    last_row = triangle[-1]  
    new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1] 
    return triangle + [new_row]  

def main(n)
    n = int(input('Введите сколько строчек треугольника Паскаля вывести:'))
    print(pascal_triangle(n))

if _name_ == '_main_':
    main()
