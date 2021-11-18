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


#create a list without range
#put function to create the piramid like in range 
my_list=[" * "," * "," * "," * "," * "]
no_print=0
for i in (my_list):
    
    print(no_print*my_list[no_print-1])
    
    no_print+=1
#half of triangle using list
    
for i in (my_list):
    
    print(no_print*my_list [no_print-1])

    no_print-=1
#triangle printed 
space=" "
variable =0
for i in (my_list):
    print (variable*space +my_list [variable])
    variable+=1
#print one external lie for the triangle 
for i in (my_list):
    print(variable*space+my_list [variable- 1])
    variable-=1
#function to print a triangle external line only 
for i in range (0, 3):
    for i in (my_list):
        print(variable*space +my_list[ variable- 1])
        variable+=1
    for i in (my_list):
         print (variable*space+my_list[ variable- 1])
         variable-=1
#whit range repet the last step to creat a loop 


