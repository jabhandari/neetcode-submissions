class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta={}

        for i in range(len(nums)):

            if target-nums[i] in dicta:
                return [dicta[target-nums[i]],i]

            dicta[nums[i]]=i