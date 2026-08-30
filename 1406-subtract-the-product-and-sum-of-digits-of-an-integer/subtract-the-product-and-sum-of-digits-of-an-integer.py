class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr_prod=1
        arr_sum=0
        temp=n
        
        while temp>0:
            r=temp%10
            arr_sum+=r
            arr_prod=arr_prod*r
            temp//=10
        return arr_prod-arr_sum