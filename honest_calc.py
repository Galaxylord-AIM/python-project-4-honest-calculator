# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
result = 0

while True:
    print(msg_0)
    calc = input()
    calc = calc.split(" ")
    try:
        x, oper, y = float(calc[0]), calc[1], float(calc[2])
        if oper == "+":
            result = x + y
            break
        elif oper == "-":
            result = x - y
            break
        elif oper == "/":
            if (oper == "/") and (y == 0):
                print(msg_3)
                continue
            result = x / y
            break
        elif oper == "*":
            result = x * y
            break
        else:
            print(msg_2)
    except:
        print(msg_1)

print(result)
