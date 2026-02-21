class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        m=s
        for r in range(k,len(nums)):
            s+=nums[r]
            s-=nums[r-k]
            m=max(m,s)
        return m/k
# Maximum Average Subarray I
        