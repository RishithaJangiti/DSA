from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        c1=Counter(s1)
        c2=Counter(s2[:n])
        if n>m:
            return False
        if c1==c2:
            return True
        for i in range(n,m):
            c2[s2[i]]+=1
            c2[s2[i-n]]-=1
            if c2[s2[i-n]]==0:
                del c2[s2[i-n]]
            if c1==c2:
                return True
        return False

        