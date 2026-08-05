class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sm, lg, ans = float("inf"), 0, []
        for i in nums:
            sm, lg = min(sm, i), max(lg,i)
        hashList = [0]*(lg-sm+1)
        print(hashList, sm, lg)
        for i in nums:
            hashList[i-sm]=1
        for i in range(len(hashList)):
            if hashList[i]==0:
                ans.append(i+sm)
        return ans
        
        