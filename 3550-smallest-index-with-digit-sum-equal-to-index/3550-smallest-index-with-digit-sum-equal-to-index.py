class Solution:
    def calculateSum(self, num) -> int:
        sum = 0
        while num:
            sum+=num%10
            num = num//10
        return sum
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==self.calculateSum(nums[i]):
                return i
        return -1
        