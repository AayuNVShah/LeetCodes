class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n, cnt=len(nums), 0
        mid = nums[n//2]
        for num in nums:
            if num==mid:cnt+=1
            if cnt>1:
                return False
        return True

        