class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCt=0
        mul=1
        for i in nums:
            if i==0:
                zeroCt+=1
            else:
                mul*=i
        res=[0]*len(nums)
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

