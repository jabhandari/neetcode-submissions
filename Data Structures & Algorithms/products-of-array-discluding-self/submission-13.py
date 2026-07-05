class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        zeroCt=0
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                zeroCt+=1
            else:
                mul*=nums[i]
        for i in range(len(nums)):
            if zeroCt>1:
                res[i]=0
            elif zeroCt==1:
                if nums[i]==0:
                    res[i]=mul
                else:
                    res[i]=0
            else:
                res[i]=mul//nums[i]
        return res