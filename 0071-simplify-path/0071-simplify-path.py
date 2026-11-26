class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[]
        p=path.split("/")
        for i in p:
            if i=="" or i==".":
                continue
            elif i=="..":
                if res:
                    res.pop()
            else:
                res.append(i)
        return "/"+"/".join(res)