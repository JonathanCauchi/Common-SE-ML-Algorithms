import math

def main():
    C = int(input("Enter C value\n"))
    H = int(input("Enter H value\n"))
    D = [i for i in input().split(",")]
    D = [int(i) for i in D]
    D = [calc(C,H,i) for i in D]
    D = [round(i) for i in D]
    D = [str(i) for i in D]
    
    print(",".join(D))
    
def calc(C,H,D):
    return math.sqrt((2*C*D)/H)

main()