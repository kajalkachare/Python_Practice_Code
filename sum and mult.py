#Calculate sum and Multiplication of two numbers.
def calculate( num1, num2):
    sum = num1+ num2
    mult= num1* num2
    return  sum,mult

sum_answer,mult_answer=calculate(10,20)
print(f"sum: {sum_answer} , mult: {mult_answer}")
