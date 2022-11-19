#function to calculate occurance

def occur(n,m):
    ans = 0
    def chk(k,l):
        chk = str(l)
        num = str(k)
        count = num.count(chk)
        return count
    while n>=0:
        ans+=chk(n,m)
        n=n-1
    return ans 

n = int(input("Enter N: "))
m = int(input("Enter M: "))

total_occur = occur(n,m)
print(total_occur)

