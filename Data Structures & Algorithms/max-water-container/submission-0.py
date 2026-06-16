class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,ans= 0,len(heights)-1,-1
        while l<r:
            cur = (r-l)*min(heights[l],heights[r])
            print(l , r ,min(heights[l],heights[r]))
            ans=max(ans,cur)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return ans
