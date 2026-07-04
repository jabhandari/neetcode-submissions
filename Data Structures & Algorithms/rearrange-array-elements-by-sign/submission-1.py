class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        posi=0
        negi=1
        for i in range(len(nums)):
            if nums[i]>0:
                res[posi]=nums[i]
                posi+=2
            else:
                res[negi]=nums[i]
                negi+=2
        return res