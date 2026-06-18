class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        ans=[]
        n=len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
               
            x,y=i+1,n-1
            while x<y:
                s=nums[i]+nums[x]+nums[y]
                if s==0:
                    ans.append([nums[i],nums[x],nums[y]])
                    while x<y and nums[x+1]==nums[x]:
                        x+=1
                    while x<y and nums[y-1]==nums[y]:
                        y-=1
                    x += 1
                    y -= 1
                elif s>0:
                    y-=1
                else:
                    x+=1
        
        return ans