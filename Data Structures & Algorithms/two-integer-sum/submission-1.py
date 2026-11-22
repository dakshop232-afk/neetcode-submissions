class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        before={}

        for i,n in enumerate(nums):
            diffrence=target-n
            if diffrence in before:
                return [before[diffrence],i]
            before[n]=i


        
        