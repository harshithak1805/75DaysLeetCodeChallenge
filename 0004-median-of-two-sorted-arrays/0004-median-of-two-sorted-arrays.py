class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        def merge(n1,n2):
            i=0
            j=0
            r=[]
            while i<len(n1) and j<len(n2):
                if n1[i]>n2[j]:
                    r.append(n2[j])
                    j+=1
                else:
                    r.append(n1[i])
                    i+=1
            r.extend(n1[i:])
            r.extend(n2[j:])
            return r
        def median(r):
            med=0
            if len(r)%2==0:
                med=(r[len(r)//2]+r[(len(r)//2)-1])/2
            else:
                med=r[len(r)//2]
            return med
        x=merge(n1,n2)
        return median(x)

        