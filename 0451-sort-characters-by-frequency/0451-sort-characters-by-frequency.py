class Solution:
    def frequencySort(self, s: str) -> str:
        freq, ans = {}, ""
        for i in s:
            freq[i]=freq.get(i,0)+1
        freq = dict(sorted(freq.items(), key=lambda item: -item[1]))
        for i in freq:
            ans+=i*freq[i]
        return ans

        