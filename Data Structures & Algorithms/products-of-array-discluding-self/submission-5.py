class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeroCt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeroCt+=1
        if zeroCt>1:
            return [0]*len(nums)

        res=[0]*len(nums)
        for i in range(len(nums)):
            if zeroCt==1:
                if nums[i]==0:
                    res[i]=prod
                else:
                    res[i]=0
            else:
                res[i]=prod//nums[i]
        return res
            
            