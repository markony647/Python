def main():
    expression = raw_input("Please input your expression: ")
    operands = expression.split()
 
    numbers = {"one":1, "two":2, "three":3}
    operations = {"plus":"+", "minus":"-"}
 
    for item in operands:
        if item in numbers:
            #replace
            operands[operands.index(item)] = str(numbers[item])
        if item in operations:
            #replace
            operands[operands.index(item)] = operations[item]
 
    concatenated_expression = "".join(operands)
    result = eval(concatenated_expression)
 
    print "Evaluate expression %s = %s" % (concatenated_expression, result)
 
if __name__ == '__main__':
    main()	