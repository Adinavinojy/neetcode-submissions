class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                index=ord(char)-ord('a')
                count[index]+=1
            t=tuple(count)
            d[t].append(word)
        return list(d.values())  