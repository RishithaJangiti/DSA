class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ch=set()
        mx_len=0
        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            mx_len=max(mx_len,r-l+1)
        return mx_len
        


        