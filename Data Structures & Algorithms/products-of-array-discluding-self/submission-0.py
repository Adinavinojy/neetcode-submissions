class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num=0
        prefix=1
        result=[]
        for i in range(len(nums)):
            result.append(prefix)
            prefix*=nums[i]
        suffix=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]
        return(result)