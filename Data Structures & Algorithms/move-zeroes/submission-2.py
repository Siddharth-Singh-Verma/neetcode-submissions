class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                t= nums[i]
                nums[i]=nums[z]
                nums[z]=t
                z+=1
