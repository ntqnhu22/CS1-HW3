print("Welcome to the calculator!")
#the def
def add(a,b):
        add=a+b
        return add
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul
def div(a, b):
    div=a/b
    return div
def exp(a,b):
    exp=a**b
    return exp 
def main():
    a=int(input('Enter your first number:'))
    b=int(input('Enter your second number:'))
    if a>=1 and a<=5 and b>=1 and b<=5 :
        print('1. Add\n2. Substract\n3. Multiply\n4. Divide\n5. Exponent')
        c=int(input('Enter your operation:'))
        if c==1:
            d=add(a,b)
            print(d)
        elif c==2:
            f=sub(a,b)
            print(f)
        elif c==3:
            g=mul(a,b)
            print(g)
        elif c==4:
            h=div(a,b)
            print(h)
        elif c==5:
            e=exp(a,b)
            print(e)
    else: 
        print("Invalid operation") 
    
if __name__ == "__main__":
    main()


