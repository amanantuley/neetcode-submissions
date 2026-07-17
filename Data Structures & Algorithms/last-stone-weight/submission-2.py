class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            cur = stones.pop() - stones.pop()

            if cur:
                stones.append(cur)

        return stones[0] if stones else 0

# First we will check the length of the stone if it is greater than 1 :
# We will sort it then it will alligned like : (0 , 1, 2 , 3)
# Then we will pop the stones so it will get poped from the last
#  then we will subtract the last two higest stones 
#  store it in a variable
# Append the variable to the stones section
# Then return the value as stones[0] -> zero index as 1 stone will only left
#  else return 0 as no stone left