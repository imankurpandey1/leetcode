class Solution:
    def sortstrings(self,s):
        st=list(s)
        st.sort()
        return "".join(st)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            key=self.sortstrings(i)
            if key in seen:
                seen[key].append(i)
            else:
                seen[key]=[i]
        return list(seen.values())
