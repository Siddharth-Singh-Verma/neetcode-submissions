class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
       
        for s in strs:
            sorteds = ''.join(sorted(s))
            res[sorteds] = res.get(sorteds, [])
            res[sorteds].append(s)

        return list(res.values())