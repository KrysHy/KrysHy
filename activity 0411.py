import random
num1 =random.randint(0,10)
num2 =random.randint(0,10)
answer = eval(input(f"What is {num1} + {num2} ="))
#####
while answer != num1+num2:
    print ("try again")
    answer = eval(input(f"What is {num1} + {num2} ="))
  
print(answer)
######
print("well done!!")
