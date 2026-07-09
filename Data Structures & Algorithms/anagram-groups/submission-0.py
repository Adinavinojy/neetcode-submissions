class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            count=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                count[index]+=1
            t=tuple(count)
            if t in d:
                d[t].append(word)
            else:
                d[t]=[word,]
        return list(d.values())  