class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            j = i+1
            while(j<len(nums)):
                if v+nums[j]==target:
                    ans=[i,j]
                    return ans
                j+=1
            
        