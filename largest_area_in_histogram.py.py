class Solution:
    def nsel(self, a, n):
        s = []
        v = []
        for i in range(n):
        
            while len(s) > 0 and s[-1][0] >= a[i]:
                s.pop()
            
            if len(s) == 0:
                v.append(-1)
            else:
                v.append(s[-1][1])
        
            s.append([a[i], i])
    
        return v
    
    def nser(self, a, n):
    
        s = []
        v = []
    
        for i in range(n-1, -1, -1):
        
            while len(s) > 0 and s[-1][0] >= a[i]:
                s.pop()
            
            if len(s) == 0:
                v.append(n)
            else:
                v.append(s[-1][1])
            
            s.append([a[i], i])
        
        v.reverse()
        return v
    
    def largestRectangleArea(self, a: List[int]) -> int:
        n  = len(a)
        nsl = self.nsel(a, n)
        nsr = self.nser(a, n)

        res = []
        for i in range(n):
            res.append(nsr[i]-nsl[i]-1)
    
        ans = []
        for i in range(n):
            ans.append(res[i]*a[i])
            
        return max(ans)
