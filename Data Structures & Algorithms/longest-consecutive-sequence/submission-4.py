class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for i in range(len(nums)):
            lenght=0
            if (nums[i]-1) not in numSet:
                lenght+=1
                while (nums[i]+lenght) in numSet:
                    lenght+=1
                longest=max(lenght,longest)
        return longest
                    
