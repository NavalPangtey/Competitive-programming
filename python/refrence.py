# Passing Immutable Object (List) 
#defining the function  
def change_list(list1):  
    list1.append(20);  
    list1.append(30);  
    print("list inside function = ",list1)  
      
    #defining the list  
list1 = [10,30,40,50]  
      
#calling the function   
change_list(list1);  
print("list outside function = ",list1);  

#Passing Mutable Object (String)

#defining the function  
def change_string (str):  
    str = str + " Hows you";  
    print("printing the string inside function :",str);  
      
string1 = "Hi I am there"  
      
#calling the function  
change_string(string1)  
      
print("printing the string outside function :",string1)  