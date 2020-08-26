# Write your code here :-)
Prev2=0
Prev1=1
for i in range(20):
 Current=Prev2+Prev1
 print(Current)
 Prev2,Prev1=Prev1,Current