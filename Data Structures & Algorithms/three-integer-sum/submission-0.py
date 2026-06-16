class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(0,n,1):
            l, r = i+1, n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                cursum= nums[i]+nums[l]+nums[r]
                if cursum>0:
                    r-=1
                elif cursum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
      
        return ans

