class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        total=m*n
        rowstart=0
        colstart=0
        rowend=m-1
        colend=n-1
        c=0
        while c<=total:
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                c+=1
            rowstart+=1
            if c==total:
                break
            for i in range(rowstart,rowend+1):
                ans.append(matrix[i][colend])
                c+=1
            colend-=1
            if c==total:
                break
            for i in range(colend,colstart-1,-1):
                ans.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break
            for i in range(rowend,rowstart-1,-1):
                ans.append(matrix[i][colstart])
                c+=1
            colstart+=1
            if c==total:
                break
        return ans
        

