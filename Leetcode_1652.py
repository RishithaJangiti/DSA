class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        
        for i in range(len(code)):
            if k==0:
                return res
            elif k>0:
                s=0
                for j in range (1,k+1):
                    s+=code[(i+j)%n]
                res[i]=s
            else:
                s=0
                for j in range(1,abs(k)+1):
                    s+=code[(i-j)%n]
                res[i]=s
        return res




        