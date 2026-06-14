class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        fs=[]
        for i in s:
            if i==")" and fs and fs[-1]=="(":
                fs.pop()
            else:
                fs.append(i)
        return len(fs)    
            

