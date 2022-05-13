if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    
    lists = []
    
    for i in a:
        if max(a) == i:
            pass
        else:
            lists.append(i)
            
    print(max(lists))
