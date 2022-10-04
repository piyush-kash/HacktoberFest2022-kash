class Solution:
    def closestPower(self,n):
        i=0
        res=0
        while 2**i<=n:
            res=2**i
            i+=1
        if (n-res)>=((2**i)-n):
            return 2**(i)
        else:
            return res
        # Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    T=int(input("Enter Number of Twimes you want to run code : "))
    for i in range(T):
        n = int(input("Enter Number : "))
        ob = Solution();
        ans = ob.closestPower(n)
        print("Two power value close to",n,"is : ",ans)
# } Driver Code Ends