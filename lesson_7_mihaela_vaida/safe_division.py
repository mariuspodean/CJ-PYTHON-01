def  safe_divide(func):
    def exception (arg1,arg2):
        try:
            if type(arg1/arg2)==int or type(arg1/arg2)==float or arg2!=0:
                print(arg1/arg2)
            
                

        except:
             print("The division cannot be performed")
    return exception        
  

@safe_divide
def divide(first_number , second_number):
    
    return first_number / second_number
    
 
