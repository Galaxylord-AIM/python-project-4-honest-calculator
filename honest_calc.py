# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

while True:
    print(msg_0)
    calc = input()
    calc = calc.split(" ")
    try:
        x, oper, y = float(calc[0]), calc[1], float(calc[2])
        if (oper == "+") or (oper == "-") or (oper == "/") or (oper == "*"):
            break
        print(msg_2)
    except:
        print(msg_1)
