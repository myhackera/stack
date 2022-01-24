#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        st = [0]
        res = [1]
        
        for i in range(1, n):
            
            while len(st) > 0 and a[st[-1]] <= a[i]:
                st.pop()
            if len(st) <= 0:
                res.append(i+1)
            else:
                res.append(i-st[-1])
            
            st.append(i)
        return res
