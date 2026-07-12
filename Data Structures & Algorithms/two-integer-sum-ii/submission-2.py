class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        n=len(numbers)
        for i in range(n):
            a=numbers[i]
            if a in d:
                return([d[a]+1,i+1])
            else:
                d[target-a]=i