#Week 5 Mini project 1.0
#number of rows with input function
"need to input 5 for this exercise "
star=int(input("How many * you think you need : "));
for i in range(star):#range function, nested loop  
    for j in range(i):#display number 
       print ('* ', end="")#new line after new row 
    print('')	
for i in range(star,0,-1):
    for j in range( i):
        print('* ', end="")
    print('')



