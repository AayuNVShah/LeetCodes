class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n, sortedArr = len(arr), sorted(set(arr))
        ht,cnt = {}, 1
        for i in sortedArr:
            ht[i]=cnt
            cnt+=1
        for i in range(n):
            arr[i]=ht[arr[i]]
        return arr
        