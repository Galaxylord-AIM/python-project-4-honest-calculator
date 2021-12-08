# start
memory = 0
result = 0


# message list
def message(msg_index_value):
    if msg_index_value == 0:
        msg_text = "Enter an equation"
    elif msg_index_value == 1:
        msg_text = "Do you even know what numbers are? Stay focused!"
    elif msg_index_value == 2:
        msg_text = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    elif msg_index_value == 3:
        msg_text = "Yeah... division by zero. Smart move..."
    elif msg_index_value == 4:
        msg_text = "Do you want to store the result? (y / n):"
    elif msg_index_value == 5:
        msg_text = "Do you want to continue calculations? (y / n):"
    elif msg_index_value == 6:
        msg_text = " ... lazy"
    elif msg_index_value == 7:
        msg_text = " ... very lazy"
    elif msg_index_value == 8:
        msg_text = " ... very, very lazy"
    elif msg_index_value == 9:
        msg_text = "You are"
    elif msg_index_value == 10:
        msg_text = "Are you sure? It is only one digit! (y / n)"
    elif msg_index_value == 11:
        msg_text = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    elif msg_index_value == 12:
        msg_text = "Last chance! Do you really want to embarrass yourself? (y / n)"

    return msg_text


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + message(6)
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + message(7)
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + message(8)
    if msg != "":
        msg = message(9) + msg

    return msg


def is_one_digit(v):
    # if float(v) == int(v):
    #     v = int(v)
    # else:
    #     v = float(v)
    if (-10 < v < 10) and v.is_integer():
        return True
    return False


while True:
    # print(memory)
    while True:
        print(message(0))
        calc = input()
        # print("input check", calc)
        calc_split = calc.split(" ")
        # print('split check', calc_split)
        x, oper, y = calc_split[0], calc_split[1], calc_split[2]
        # print('y =', y)
        # print('operator =', oper)
        # print('x =', x)

        if x == 'M':
            x = memory
            # print('value changed for x = ', x)
        if y == 'M':
            y = memory
            # print(type(y))
            # print('value changed for y = ', y)
        try:
            x, y = float(x), float(y)
            # print(type(x), type(y))
            # print(x, y)
            # if float(x) == int(x):
            #     x = int(x)
            # else:
            #     x = float(x)
            # if float(y) == int(y):
            #     y = int(y)
            # else:
            #     y = float(y)
            # print(type(x), '--->', x)
            # print(type(y), '--->', y)
        except ValueError:
            print(message(1))

        if (oper == "+") or (oper == "-") or (oper == "*") or (oper == "/"):
            print(check(x, y, oper))
            if oper == "+":
                result = float(x) + float(y)
                # print(result)
                break
            elif oper == "-":
                result = x - y
                # print(result)
                break
            elif oper == "*":
                result = x * y
                # print(result)
                break
            else:
                if (oper == "/") and (y == 0):
                    print(message(3))
                    continue
                else:
                    result = x / y
                    # print(result)
                    break
        else:
            print(message(2))
    # if float(result) == int(result):
    #     result = int(result)
    # else:
    #     result = float(result)
    print(result)
    while True:
        # print(memory)
        print(message(4))
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(message(msg_index))
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
                    else:
                        continue
            else:
                memory = result

            # print(result)
            # print(memory)
            break
        elif answer == 'n':
            break

    while True:
        print(message(5))
        answer = input()
        if answer == 'y':
            break
        elif answer == 'n':
            exit(0)
