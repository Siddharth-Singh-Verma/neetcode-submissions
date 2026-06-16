class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        s=[]
        x="abcdefghijklmnopqrstuvwxyz0123456789"
        for c in t:
            if c in x:
                s.append(c)

        print(s)
        l,r=0,len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True