class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCt=0
        prod=1
        for i in nums:
            if i==0:
                zeroCt+=1
            else:
                prod*=i
        res=[0]*len(nums)
        for i in range(len(nums)):
            if zeroCt>1:
                res[i]=0
            elif zeroCt==1:
                if nums[i]==0:
                    res[i]=prod
                else:
                    res[i]=0
            else:
                res[i]=prod//nums[i]
        return res