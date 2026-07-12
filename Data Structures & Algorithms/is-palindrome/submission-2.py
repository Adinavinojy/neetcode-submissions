class Solution:
    def isPalindrome(self, s: str) -> bool:
        def pal(s,n,m):
            if n-1==m or n==m:
                return True
            elif s[n]==s[m]:
                return pal(s,n+1,m-1)
            else:
                return False
        s1="".join([i.lower() for i in s if i.isalnum()])
        print(s1)
        return pal(s1,0,len(s1)-1)
        