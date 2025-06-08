def perform_operation(num1, num2, operation):
    if operation == 'divide':
        if num2 == 0 :
            return "cannot divide by zero"
        else:
            result = num1 / num2
    elif operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2

    else:
        return "invalid operation"



    return result


values = perform_operation(10, 0, "divide")
print(values)
