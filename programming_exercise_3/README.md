# Programming Exercise 3: Function Scope and Code Optimization

Analyze the following code and answer these questions:

```python
def myFunc(a, b):
    result = a*b
    print("Result is {}".format(result))

if __name__ == "__main__":
    result = 12  # initial value
    myFunc(2,3)
    ### TODO: What is the value of "result" here ?
```

**Questions:**
1. What is the value of "result" at the TODO line?
2. Why is the value the same or different from the initial value?
3. What recommended change would you make to this code? And why?

## 1. Answer for Question 1

**The value of "result" at the TODO line is 12.**

This is the same as the initial value that was assigned at the beginning of the program.

## 2. Answer for Question 2

**The value remains the same (12) because of Python's variable scope rules:**

### What happens in the code:
1. **Global scope:** `result = 12` creates a variable in the global scope
2. **Function call:** `myFunc(2,3)` is called
3. **Local scope:** Inside the function, `result = a*b` creates a **new local variable** (not the global one)
4. **Calculation:** The local `result` gets the value `2 * 3 = 6`
5. **Function ends:** The local `result` disappears when the function exits
6. **Global scope:** The global `result` remains unchanged at 12

### The Scope Issue:
- **Variable Shadowing:** The local `result` inside the function "hides" the global `result`
- **No Return Value:** The function calculates `6` but doesn't return it to the global scope
- **No Assignment:** The global `result` is never modified by the function call

## 3. Answer for Question 3

### Changes I Made and Reasons:

#### **Change 1: Function Name**
**From:** `myFunc(a, b)`
**To:** `multiply_two_numbers(a, b)`
**Reason:** More descriptive name that clearly indicates what the function does. Function names should be self-documenting.

#### **Change 2: Return Statement**
**From:** `print("Result is {}".format(result))`
**To:** `return result`
**Reason:** 
- Functions should return values, not just print them
- This makes the function reusable in other calculations
- Follows the principle that functions should have clear inputs and outputs
- Avoids side effects and makes the function predictable

#### **Change 3: Assignment of Return Value**
**From:** `myFunc(2,3)` (no assignment)
**To:** `result = multiply_two_numbers(2,3)`
**Reason:**
- Explicitly captures the function's return value
- Makes the intention clear - we want to use the calculated result
- Eliminates scope confusion - now we know which `result` we're referring to

#### **Change 4: String Formatting**
**From:** `print("Result is {}".format(result))`
**To:** `print(f"Result is {result}")`
**Reason:**
- F-strings are more readable and modern Python syntax
- Better performance than `.format()` method
- Cleaner and more intuitive syntax

#### **Change 5: Print Location**
**From:** Print inside the function
**To:** Print in the main block after assignment
**Reason:**
- Separates calculation from presentation
- Makes the function pure (no side effects)
- Allows flexibility in how the result is used or displayed

### Results:
- **Original code:** `result = 12` (unchanged)
- **Optimized code:** `result = 6` (function result properly assigned)

