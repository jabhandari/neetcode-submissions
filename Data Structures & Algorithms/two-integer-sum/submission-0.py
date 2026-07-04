class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta={}

        for i in range(len(nums)):

            if nums[i] in dicta:
                return [dicta[nums[i]],i]

            dicta[target-nums[i]]=i