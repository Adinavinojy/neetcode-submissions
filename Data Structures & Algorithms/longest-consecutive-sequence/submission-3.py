class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        result=0
        for i in ns:
            sol=1
            if i-1 not in nums:
                cr=i
            else:
                cr=i-1
            while cr+1 in nums:
                sol+=1
                cr+=1
            result=max(result,sol)
        return result