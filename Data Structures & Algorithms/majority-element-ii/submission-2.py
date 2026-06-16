class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        counts = defaultdict(int)
        x=(len(nums)//3)+1
        for i in nums:
            counts[i]+=1
            if counts[i]==x:
                ans.append(i)
        print(counts)
        return ans