class Solution:
    def nextLargerElement(self,arr,n):
        s = []
        v = []
        for i in range(n-1, -1, -1):
          
            while(len(s) != 0 and s[-1] <= arr[i]):
                s.pop()
                
            if(len(s) == 0):
                v.append(-1)
            else:
                v.append(s[-1])
                
            s.append(arr[i])
            
        v.reverse()
        return v
