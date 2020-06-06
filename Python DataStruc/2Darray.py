def main():
    final = []
    X = int(input())
    Y = int(input())
    for i in range(X):
        list=[]
        for j in range(Y):
            list.append(i*j)
        final.append(list)
    print(final)

main()