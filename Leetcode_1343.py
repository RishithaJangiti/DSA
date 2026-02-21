class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        mx_len=0
        c=0
        s=sum(arr[:k])
        y=s/k
        if y>=threshold:
            c+=1
        for r in range(k,len(arr)):
            s+=arr[r]
            s-=arr[l]
            l+=1
            m=s/k
            if m>=threshold:
                c+=1
                mx_len=max(mx_len,c)
        return c
# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold