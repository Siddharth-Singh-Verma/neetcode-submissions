class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        ans = [0]*2
        while l<r :
            sumlr = numbers[l]+numbers[r]
            print (sumlr)
            if target == sumlr :
                ans[0]=l+1
                ans[1]=r+1
                return ans
            elif sumlr > target:
                r-=1
            else:
                l+=1
        return ans
