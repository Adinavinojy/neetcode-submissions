class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_d={}
        t_d={}
        for i in s:
            if i in s_d:
                s_d[i]+=1
            else:
                s_d[i]=1
        for i in t:
            if i in t_d:
                t_d[i]+=1
            else:
                t_d[i]=1
        return s_d == t_d