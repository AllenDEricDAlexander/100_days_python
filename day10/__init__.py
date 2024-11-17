# function & output
def format_name(first_name, last_name):
    first_name.title()
    last_name.title()
    return first_name + " " + last_name


print(format_name("james", "bond"))

operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

operation_symbol = "add"

calculation_function = operations[operation_symbol]

print(calculation_function(2, 3))
