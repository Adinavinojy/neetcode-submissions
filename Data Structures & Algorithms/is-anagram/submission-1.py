class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s=set(s)
        s_d={i:s.count(i) for i in s_s}
        t_s=set(t)
        t_d={i:t.count(i) for i in t_s}
        if t_d==s_d:
            return True
        return False