class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1
                k=len(nums)-1
                while j<k:
                    ans=nums[i]+nums[j]+nums[k]
                    if ans==0:
                        res.append([nums[i],nums[j],nums[k]])
                        j+=1
                        while nums[j]==nums[j-1] and j<k:
                            j+=1
                    elif ans<0:
                        j+=1
                    else:
                        k-=1
        return res
                