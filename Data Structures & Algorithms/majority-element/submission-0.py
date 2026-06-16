class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        ans,temp=0,float('-inf')
        
        for i in counts:
            
            if counts[i]>temp:
                temp=counts[i]
                ans=i
        return ans