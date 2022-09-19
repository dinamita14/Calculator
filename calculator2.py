def calc(num1,op,num2):
    while op == "+":
        return float(num1) + (num2)
    while op == "-":
        return float(num1) - float(num2)
    while op == "/":
        return float(num1) / float(num2)
    while op == "*":
        return float(num1) * float(num2)
print(calc(num1=input("Enter a number: "),op=input("Enter a operator: "),num2=input("Enter a number: ")))


