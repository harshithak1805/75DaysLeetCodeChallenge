class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq={}
        j=0
        ans=0
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
            while freq[s[i]]>2:
                freq[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans
