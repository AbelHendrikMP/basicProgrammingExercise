
#the input for get the variable to operate
var_1 = float(input("insert the first variable: "))
var_2 = float(input("insert the second variable: "))
print (f""" chose the operation
       1. summ (+)
       2. subtraction (-)
       3. multiplication (*)
       4. division (/)
""")
#the operator function
operation = int(input("insert the operation: "))
if operation == 1:
        print("the result is", {var_1 + var_2})
elif operation == 2:
        print("the result is", var_1 - var_2)
elif operation == 3:
        print("the result is", var_1 * var_2)
elif operation == 4 :
        print("the result is", var_1 / var_2)