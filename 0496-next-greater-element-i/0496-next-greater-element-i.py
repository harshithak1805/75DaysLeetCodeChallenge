class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            idx=nums2.index(i)
            for j in range(idx,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res