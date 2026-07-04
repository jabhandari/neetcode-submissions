class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)//2
        res={}
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]]=1
            else:
                res[nums[i]]+=1
        for key in res:
            if res[key]>maj:
                return key
        