class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1!=n2:
            return False
        freqS, freqT = [0 for i in range(26)], [0 for i in range(26)]
        for i in range(n1):
            freqS[ord(s[i])-97]+=1
            freqT[ord(t[i])-97]+=1
        for i in range(26):
            if freqS[i]!=freqT[i]:
                return False
        return True
        