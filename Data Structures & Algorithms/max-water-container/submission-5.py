class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        l=0
        r=len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                currArea=heights[l]*(r-l)
                l+=1
            else:
                currArea=heights[r]*(r-l)
                r-=1
            area=max(area,currArea)
        return area