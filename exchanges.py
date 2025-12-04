def main():
    def exchanges(list):
        
        if  len(list) == 0:
            return [[]]
        exch = []
        
        for i in range(len(spis)): 
            numb = list[i]
            remaning = list[:i] + list[i + 1:]
            exchanges_remain = exchanges(remaning)
            
            for z in exchanges_remain:
                exch.append([numn] + z)
        return exch
        
    for i in exchanges([1, 2, 3]):
        print(i)
        
if __name__ == '__main__':
    main()

