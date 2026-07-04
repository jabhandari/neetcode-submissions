class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=set(nums)
        longest=0
        for i in range(len(nums)):
            length=0
            if nums[i]-1 not in res:
                length+=1
                while nums[i]+length in res:
                    length+=1
                longest=max(longest,length)
        return longest