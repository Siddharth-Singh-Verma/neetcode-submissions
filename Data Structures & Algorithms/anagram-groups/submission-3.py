class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        n=len(strs)
        visted=set()
        for s in range(n):
            t=sorted(strs[s])
            g=[]
            g.append(strs[s])
            if s not in visted:
                for i in range(s+1,n):
                    if t==sorted(strs[i]) and i not in visted:
                        g.append(strs[i])
                        visted.add(i)
                ans.append(g)
        return ans