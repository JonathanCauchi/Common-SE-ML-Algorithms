def main():
    dict = {}
    num = int(input("Enter number"))
    for i in range(1,num+1):
        dict[i] = i*i
    print(dict)
    
main()