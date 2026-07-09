class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        bucket=[[] for _ in range(len(nums)+1)]
        for i in d:
            bucket[d[i]].append(i)
        l=[]
        for i in range(len(bucket)-1,-1,-1):
            if(len(l)==k):
                    return l
            if bucket[i]==[]:
                continue
            if len(l)+len(bucket[i])<=k:
                l.extend(bucket[i])
            else:
                c=k-len(l)
                l.extend(bucket[0:c])
