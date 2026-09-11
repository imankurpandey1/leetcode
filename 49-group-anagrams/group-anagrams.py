class Solution:
    def sortStrings(self,s):
        st=list(s)
        st.sort()
        return "".join(st)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            key=self.sortStrings(i)
            if key in dic:
                dic[key].append(i)
            else:
                dic[key]=[i]
        return list(dic.values())
