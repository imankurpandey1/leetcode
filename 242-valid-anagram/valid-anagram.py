class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        if len(s)!=len(t):
            return False

        for i in s:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i]+=1
        for j in t:
            if j not in freq2:
                freq2[j]=1
            else:
                freq2[j]+=1
        
        if freq1==freq2:
            return True
        else:
            return False