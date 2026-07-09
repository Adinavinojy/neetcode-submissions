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
                    print(len(l),k)
                    return l
            for j in bucket[i]:
                l.append(j)
                if(len(l)==k):
                    print(len(l),k)
                    return l
            

        return [0]