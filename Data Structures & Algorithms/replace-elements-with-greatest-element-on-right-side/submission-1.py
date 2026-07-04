class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxR=-1
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i]
            arr[i]=maxR
            maxR=max(maxR,temp)
        return arr 