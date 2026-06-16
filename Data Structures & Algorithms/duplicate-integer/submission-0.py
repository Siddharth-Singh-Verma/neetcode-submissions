class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tem = set(nums)
        if len(tem)==len(nums):
            return False
        return True
        