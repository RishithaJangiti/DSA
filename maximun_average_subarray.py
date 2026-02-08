class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        x=sum(nums[:k])
        mx_len=x
        for r in range(k,len(nums)):
            x+=nums[r]
            x-=nums[r-k]
            mx_len=max(x,mx_len)
        return mx_len/k

        