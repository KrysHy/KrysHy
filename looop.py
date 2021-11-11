My_list = [30,21 ,16,78,109,1,4,52]
largest = 0 #save from 0 , we haven't seen any valeus yet.
def find_max(list):
    largest=0#local variable (only avaleble while w=the function scoop 
    #global largest#refer to a variable outside of the function scope 
    for value in list:
        if value > largest:
            largest = value
        #if it isn't the largest valeu we ve seen so far , do nothing
    print(largest)
    #need befor print(largest)
    
find_max(My_list)
print (type(find_max(My_list)))

#if find_max(My_list)% 2 == 0 :
#    print("True")
#else:
#    print("False")
