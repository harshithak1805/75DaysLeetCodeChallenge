class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ml=0
        for i in range(n):
            seen=[]
            for j in range(i,n):
                if s[j] in seen :
                    break
                seen.append(s[j])
                l=j-i+1
                ml=max(ml,l)
        return ml