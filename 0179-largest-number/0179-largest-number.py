class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=len(nums)
        ele=[""]*n
        res=""
        for i in range(n):
            ele[i]=str(nums[i])
        i=0
        j=1
        for i in range(n):
            for j in range(i+1,n):
                if ele[i]+ele[j]>ele[j]+ele[i]:
                    j+=1
                else:
                    ele[i],ele[j]=ele[j],ele[i]
        res="".join(ele)
        if res[0]=="0":
            res="0"
        return res