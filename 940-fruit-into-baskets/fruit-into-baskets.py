class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        basket={}
        for right in range(len(fruits)):
            fruit=fruits[right]
            
            if fruit in basket:
                basket[fruit]+=1
            else:
                basket[fruit]=1
            if len(basket)>2:
                left_fruit=fruits[left]
                basket[left_fruit]-=1

                if basket[left_fruit]==0:
                    del basket[left_fruit]

                left+=1
        return len(fruits)-left