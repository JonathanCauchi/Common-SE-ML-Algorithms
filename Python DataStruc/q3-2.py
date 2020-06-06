def main():
    num = int(input("Enter number\n"))
    result = {i: i*i for i in range(1,num+1)}
    print(result)
    
main()