def main():
    def exchanges(spis):
        if  len(spis) == 0:
            return [[]]
        all_exchanges = []
        for i in range(len(spis)): 
            numb_one = spis[i]
            remaning = spis[:i] + spis[i + 1:]
            exchanges_remain = exchanges(remaning)
            for z in exchanges_remain:
                all_exchanges.append([numb_one] + z)
        return all_exchanges
    for i in exchanges([1, 2, 3]):
        print(i)
if __name__ == '__main__':
    main()
