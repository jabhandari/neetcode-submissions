class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zeroct=1,0
        for i in nums:
            if i!=0:
                prod*=i
            else:
                zeroct+=1
        if zeroct>1:
            return [0]*len(nums)

        res=[0]*len(nums)
        for i in range(len(nums)):
            if zeroct==1:
                if nums[i]==0:
                    res[i]=prod
                else:
                    res[i]=0
            else:
                res[i]=prod//nums[i]
        return res
            