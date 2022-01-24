string_op ="rarrar"
half_String = int(len(string_op)/2)

if len(string_op) %2== 0:
    first_string_op =  string_op[:half_String]
    second_string_op = string_op[half_String:]
else :
    first_string_op = string_op  [:half_String]
    second_string_op = string_op[half_String+1:]
if first_string_op == second_string_op:
    print("this Number is symatrical")
else:
    print(" it is not symetrical")
    
if first_string_op == second_string_op[::-1]:
    print ("It is a palindrome")
else:
    print ("THIs number is not plaindrome")
    
    
 

