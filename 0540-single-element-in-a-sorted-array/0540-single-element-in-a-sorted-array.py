class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            if mid>0 and nums[mid]==nums[mid-1]:
                if mid%2==1:
                    l = mid+1
                else:
                    r = mid-1
            elif nums[mid]==nums[mid+1]:
                if mid%2==1:
                    r = mid-1
                else:
                    l = mid+1
            else:
                return nums[mid]
        return nums[l]
        