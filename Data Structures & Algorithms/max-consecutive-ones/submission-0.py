class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=0
        long=0
        for i in nums:
            if i==1:
                long+=1
            else:
                long=0
            length=max(length,long)            
        return length
