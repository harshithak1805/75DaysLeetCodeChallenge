class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seenst={}
        seents={}
        for i in range(len(s)):
            if s[i] not in seenst:
                seenst[s[i]]=t[i]
            else:
                if t[i]!=seenst[s[i]]: 
                    return False
        for i in range(len(s)):
            if t[i] not in seents:
                seents[t[i]]=s[i]
            else:
                if s[i]!=seents[t[i]]: 
                    return False
        return True
                    