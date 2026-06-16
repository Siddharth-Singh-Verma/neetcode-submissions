class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        sz=float('inf')
        for s in strs:
            sz=min(sz,len(s))
        
        for i in range(0,sz):
            ch=strs[0][i]
            for j in range(1,len(strs)):
                if ch !=strs[j][i]:
                    return ans
            ans+=ch
        return ans
