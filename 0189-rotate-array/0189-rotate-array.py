class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k=k%n
        # [4,3,2,1,7,6,5]
        # [5,6,7,1,2,3,4]
        def reverse(i, j):
            while i<j:
                nums[i],nums[j]=nums[j], nums[i]
                i+=1
                j-=1
        reverse(0,n-k-1)
        reverse(n-k,n-1)
        reverse(0,n-1)
        