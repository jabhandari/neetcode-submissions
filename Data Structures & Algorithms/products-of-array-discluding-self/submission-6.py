class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeroCt=0
        for num in nums:
            if num!=0:
                prod*=num
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
            