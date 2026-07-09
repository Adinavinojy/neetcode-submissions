class Solution:

    def encode(self, strs: List[str]) -> str:
        length=[len(i) for i in strs]
        s=""
        for i in range(len(strs)):
            s+=str(length[i])+"#"+strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        length=0
        num=0
        l=[]
        while num<len(s):
            temp=""
            while s[num]!="#":
                temp+=s[num]
                num+=1
            length=int(temp)
            temp=s[num+1:num+length+1]
            l.append(temp)
            num+=length+1
        print(l)
        return l


            