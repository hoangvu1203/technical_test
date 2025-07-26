def multiply_two_numbers(a, b): # change from myFunc to multiply_two_numbers for meaningful name
    result = a*b
    # return the result instead of printing it
    return result
    
if __name__ == "__main__":
    result = 12  # initial value
    result = multiply_two_numbers(2,3) # call the function and assign the result to the variable result
    # so the value of "result" here will be 6
    print(f"Result is {result}") # using f-strings instead of .format()
