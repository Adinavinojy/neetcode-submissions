class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in numbers:
            if i in d:
                return([d[i]+1,numbers.index(i)+1])
            else:
                d[target-i]=numbers.index(i)