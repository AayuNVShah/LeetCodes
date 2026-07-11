class Solution:
    def search(self, nums: List[int], target: int) -> int:
        root, n = 0, len(nums)
        l, r = 0, n-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        root, l, r = l, 0, n-1
        while l<=r:
            mid = l+(r-l)//2
            val = (mid+root)%n
            if nums[val]==target:
                return val
            if nums[val]<target:
                l = mid+1
            else:
                r = mid-1
        return -1


            