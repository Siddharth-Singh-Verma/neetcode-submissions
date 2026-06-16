class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        seen[nums[0]]=0
        ans=[]
        for i in range(1,len(nums)):
            if target-nums[i] in seen:
                ans.append(seen[target-nums[i]])
                ans.append(i)
                break
            else:
                seen[nums[i]]=i
        return ans

