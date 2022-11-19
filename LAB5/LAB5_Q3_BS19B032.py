#x power n function

def power(x,n):
    ans = 1
    if n==0:
        return 1
    else:
        if n>0:
            for i in range(n):
                ans = ans*x
            return ans
        else:
            n = n*-1
            for i in range(n):
                ans = ans*x
            return (1/ans)

x = int(input("Enter number to calculate power: "))
print("")
n = int(input("Enter the power to be raised: "))
print("")

power_x = power(x,n)
print(power_x)
        
